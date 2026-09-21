#!/usr/bin/env node
/* Homepage capability search: query params fill the box and chips, and
   input/chip changes write the URL with replaceState. No browser, no network. */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const root = path.resolve(process.argv[2] || __dirname);
const problems = [];

function chip(kind, val) {
  return {
    attrs: { "data-kind": kind, "data-val": val, "aria-pressed": "false" },
    listeners: {},
    getAttribute(k) { return this.attrs[k]; },
    setAttribute(k, v) { this.attrs[k] = String(v); },
    addEventListener(ev, fn) { this.listeners[ev] = fn; },
    click() { if (this.listeners.click) this.listeners.click(); },
  };
}

function boot(search) {
  const chips = [
    chip("mcp", "official"),
    chip("mcp", "community"),
    chip("gate", "free"),
    chip("gate", "paid"),
    chip("cli", "any"),
  ];
  const qEl = { value: "", listeners: {}, addEventListener(ev, fn) { this.listeners[ev] = fn; } };
  const out = { innerHTML: "" };
  const cnt = { textContent: "" };
  const stamp = { textContent: "" };
  const byId = { q: qEl, results: out, count: cnt, idxstamp: stamp };
  const document = {
    getElementById(id) { return byId[id] || null; },
    querySelectorAll(sel) { return sel === ".chip" ? chips : []; },
  };
  const loc = { pathname: "/gtm-directory/", search: search || "", hash: "" };
  const history = {
    replaceState(_a, _b, href) {
      const u = new URL(href, "https://andrewcmcguire.com");
      loc.pathname = u.pathname;
      loc.search = u.search;
      loc.hash = u.hash;
    },
  };
  const window = { document, history, location: loc, GTMD_INDEX: undefined };
  const ctx = {
    window,
    document,
    history,
    location: loc,
    console,
    Array,
    String,
    URLSearchParams,
  };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, "assets", "search-index.js"), "utf8"), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, "assets", "search.js"), "utf8"), ctx);
  return { qEl, chips, out, loc, type(v) {
    qEl.value = v;
    if (qEl.listeners.input) qEl.listeners.input();
  } };
}

function pressed(chips, kind, val) {
  const c = chips.find((x) => x.getAttribute("data-kind") === kind && x.getAttribute("data-val") === val);
  return c && c.getAttribute("aria-pressed") === "true";
}

function params(search) {
  return Object.fromEntries(new URLSearchParams(search));
}

const deep = boot("?q=apollo&mcp=official");
if (deep.qEl.value !== "apollo") problems.push("q input is " + JSON.stringify(deep.qEl.value));
if (!pressed(deep.chips, "mcp", "official")) problems.push("official MCP chip not pressed on load");
if (!/apollo/i.test(deep.out.innerHTML)) problems.push("results after ?q=apollo&mcp=official lack Apollo");

deep.type("hubspot");
let qs = params(deep.loc.search);
if (qs.q !== "hubspot") problems.push("typing hubspot left search " + deep.loc.search);
if (qs.mcp !== "official") problems.push("mcp dropped after typing: " + deep.loc.search);

deep.chips.find((c) => c.getAttribute("data-kind") === "gate" && c.getAttribute("data-val") === "free").click();
qs = params(deep.loc.search);
if (qs.gate !== "free") problems.push("free chip did not set gate=free: " + deep.loc.search);

deep.chips.find((c) => c.getAttribute("data-kind") === "mcp" && c.getAttribute("data-val") === "official").click();
qs = params(deep.loc.search);
if (qs.mcp) problems.push("toggling official off left mcp in URL: " + deep.loc.search);

deep.chips.find((c) => c.getAttribute("data-kind") === "cli").click();
qs = params(deep.loc.search);
if (qs.cli !== "1") problems.push("CLI chip did not set cli=1: " + deep.loc.search);

const bogus = boot("?q=enrich&mcp=not-a-real-bucket");
if (bogus.qEl.value !== "enrich") problems.push("invalid mcp URL did not keep q=enrich");
if (pressed(bogus.chips, "mcp", "official")) problems.push("unknown mcp value invented official");
if (params(bogus.loc.search).mcp) problems.push("unknown mcp value was written back: " + bogus.loc.search);

if (problems.length) {
  console.error("CHECK FAILED");
  for (const p of problems) console.error("  " + p);
  process.exit(3);
}
console.log("check_search_url: deep-link, replaceState, and unknown mcp ignore all passed");
