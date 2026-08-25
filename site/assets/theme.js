/* Loaded blocking in <head> so the stored theme is applied before first paint.
   Kept in its own file, not inline, so the Content-Security-Policy in _headers can
   forbid inline script outright. */
(function(){
  try{
    var t=localStorage.getItem('gtmd-theme');
    if(t){document.documentElement.setAttribute('data-theme',t);}
  }catch(e){}
})();
function gtmdWireToggle(){
  var b=document.getElementById('themetoggle');
  if(!b)return;
  function cur(){
    var a=document.documentElement.getAttribute('data-theme');
    if(a)return a;
    return window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
  }
  function paint(){b.textContent=cur()==='dark'?'Light':'Dark';}
  b.addEventListener('click',function(){
    var n=cur()==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',n);
    try{localStorage.setItem('gtmd-theme',n);}catch(e){}
    paint();
  });
  paint();
}
if(document.readyState==='loading'){
  document.addEventListener('DOMContentLoaded',gtmdWireToggle);
}else{gtmdWireToggle();}
