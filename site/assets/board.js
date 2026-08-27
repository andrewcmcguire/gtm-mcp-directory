/* The GTM Engineer job board - client side filtering.
   Every row is already in the HTML. This only hides rows, so the board is complete
   and readable with JavaScript switched off, and nothing is fetched at any point. */
(function(){
  var rows = Array.prototype.slice.call(document.querySelectorAll('.jrow'));
  if(!rows.length) return;
  var q = document.getElementById('jq');
  var cnt = document.getElementById('jcount');
  var empty = document.getElementById('jempty');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.jchip'));
  var f = {fam:null, sen:null, rem:null, reg:null};

  function pass(el){
    if(f.fam && el.getAttribute('data-fam') !== f.fam) return false;
    if(f.sen && el.getAttribute('data-sen') !== f.sen) return false;
    if(f.rem && el.getAttribute('data-rem') !== f.rem) return false;
    if(f.reg && (' ' + el.getAttribute('data-reg') + ' ').indexOf(' ' + f.reg + ' ') === -1) return false;
    var t = (q && q.value ? q.value : '').trim().toLowerCase();
    if(t){
      var words = t.split(/\s+/), hay = el.getAttribute('data-q') || '';
      for(var i=0;i<words.length;i++){ if(hay.indexOf(words[i]) === -1) return false; }
    }
    return true;
  }

  function run(){
    var n = 0;
    for(var i=0;i<rows.length;i++){
      var ok = pass(rows[i]);
      rows[i].style.display = ok ? '' : 'none';
      if(ok) n++;
    }
    if(cnt) cnt.textContent = n + ' of ' + rows.length + ' shown';
    if(empty) empty.style.display = n ? 'none' : 'block';
  }

  if(q) q.addEventListener('input', run);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      var k = c.getAttribute('data-k'), v = c.getAttribute('data-v');
      var on = c.getAttribute('aria-pressed') === 'true';
      chips.forEach(function(o){
        if(o.getAttribute('data-k') === k) o.setAttribute('aria-pressed','false');
      });
      f[k] = on ? null : v;
      c.setAttribute('aria-pressed', on ? 'false' : 'true');
      run();
    });
  });
  var clear = document.getElementById('jclear');
  if(clear) clear.addEventListener('click', function(){
    f = {fam:null, sen:null, rem:null, reg:null};
    chips.forEach(function(o){ o.setAttribute('aria-pressed','false'); });
    if(q) q.value = '';
    run();
  });
  run();
})();