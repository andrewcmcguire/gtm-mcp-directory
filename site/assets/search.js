/* The GTM MCP Directory - capability search.
   Runs entirely in the page over the baked index. No backend, no network call,
   no query logging, works with the network cable pulled out. */
(function(){
  var IDX = (window.GTMD_INDEX && window.GTMD_INDEX.tools) || [];
  var META = (window.GTMD_INDEX && window.GTMD_INDEX.meta) || {};
  var q = document.getElementById('q');
  var out = document.getElementById('results');
  var cnt = document.getElementById('count');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  if(!q || !out) return;

  var filters = {mcp:null, gate:null};

  function tokens(s){
    return (s||'').toLowerCase().replace(/[^a-z0-9+.# ]+/g,' ').split(/\s+/)
      .filter(function(t){ return t.length > 1 && STOP.indexOf(t) === -1; });
  }
  var STOP = ['the','and','for','with','that','this','from','can','you','your','our','all',
              'want','need','get','use','using','tool','tools','how','what','which','does',
              'has','have','are','was','one','into','out','who','when','who','its','it'];

  function score(t, toks){
    if(!toks.length) return 1;
    var name = t.n.toLowerCase();
    var s = 0, hit = 0;
    for(var i=0;i<toks.length;i++){
      var w = toks[i], any = false;
      if(name.indexOf(w) !== -1){ s += 14; any = true; }
      if(t.c.toLowerCase().indexOf(w) !== -1){ s += 5; any = true; }
      var n = 0, p = t.x.indexOf(w);
      while(p !== -1 && n < 6){ n++; p = t.x.indexOf(w, p + w.length); }
      if(n){ s += 2 + n; any = true; }
      if(any) hit++;
    }
    if(hit < toks.length) s = s * 0.35;   // partial matches sink, they do not vanish
    if(name === toks.join(' ')) s += 500; // exact name match pins to the top
    return s;
  }

  function pass(t){
    if(filters.mcp && t.m !== filters.mcp) return false;
    if(filters.gate && t.g !== filters.gate) return false;
    return true;
  }

  function esc(s){
    return String(s).replace(/[&<>"]/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
    });
  }

  var MCPTONE = {'official':'gold','community':'teal','none-found':'copper',
                 'unknown':'mute','n-a':'mute'};
  var GATETONE = {'free':'teal','paid':'gold','enterprise-leaning':'copper',
                  'enterprise-only':'copper','unknown':'mute','n-a':'mute'};

  function render(list, total){
    if(!list.length){
      out.innerHTML = '<li class="row"><div class="desc">Nothing in the index matches that. ' +
        'Try a plainer phrase, or browse by category, gate or MCP status. ' +
        'An empty result is a real answer here: it means no entry carries those words.</div></li>';
      cnt.textContent = '0 of ' + total + ' shown';
      return;
    }
    var html = '';
    for(var i=0;i<list.length;i++){
      var t = list[i];
      html += '<li class="row"><div class="top">' +
        '<a class="nm" href="tools/' + esc(t.s) + '.html">' + esc(t.n) + '</a>' +
        '<span class="dom">' + esc(t.d) + '</span></div>' +
        '<div class="desc">' + esc(t.w) + '</div>' +
        '<div class="badges">' +
        '<span class="badge ' + (MCPTONE[t.m]||'mute') + '">' + esc(t.ml) + '</span>' +
        '<span class="badge ' + (GATETONE[t.g]||'mute') + '">' + esc(t.gl) + '</span>' +
        '<span class="badge mute flat">' + esc(t.c) + '</span>' +
        '<span class="badge tier flat">' + esc(t.t) + '</span>' +
        '</div></li>';
    }
    out.innerHTML = html;
    cnt.textContent = list.length + ' of ' + total + ' shown';
  }

  var LIMIT = 60;
  function run(){
    var toks = tokens(q.value);
    var pool = IDX.filter(pass);
    var scored = [];
    for(var i=0;i<pool.length;i++){
      var sc = score(pool[i], toks);
      if(toks.length && sc <= 0) continue;
      scored.push([sc, pool[i]]);
    }
    // published ordering: relevance band first, then the fixed directory sort rule.
    scored.sort(function(a,b){
      if(!toks.length) return a[1].r - b[1].r;
      if(b[0] !== a[0]) return b[0] - a[0];
      return a[1].r - b[1].r;
    });
    var list = scored.map(function(p){ return p[1]; });
    var total = list.length;
    render(list.slice(0, LIMIT), total);
    if(total > LIMIT){
      cnt.textContent = LIMIT + ' of ' + total + ' shown. ' +
        (total - LIMIT) + ' trimmed by the display limit, not by ranking.';
    }
  }

  q.addEventListener('input', run);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      var kind = c.getAttribute('data-kind'), val = c.getAttribute('data-val');
      var on = c.getAttribute('aria-pressed') === 'true';
      chips.forEach(function(o){
        if(o.getAttribute('data-kind') === kind) o.setAttribute('aria-pressed','false');
      });
      filters[kind] = on ? null : val;
      c.setAttribute('aria-pressed', on ? 'false' : 'true');
      run();
    });
  });

  var stamp = document.getElementById('idxstamp');
  if(stamp && META.generated_on){
    stamp.textContent = META.tools + ' unique products indexed, baked ' + META.generated_on +
      ' from ' + META.entries + ' directory entries.';
  }
  run();
})();