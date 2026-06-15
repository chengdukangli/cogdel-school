/* === 语言切换 === */
function switchLang(lang) {
  const path = window.location.pathname;
  let newPath;
  if (path.includes('/en/')) {
    newPath = path.replace('/en/', '/' + lang + '/');
  } else if (path.includes('/zh/')) {
    newPath = path.replace('/zh/', '/' + lang + '/');
  } else {
    newPath = '/' + lang + '/';
  }
  window.location.href = newPath;
}

/* === 移动端菜单 === */
document.addEventListener('DOMContentLoaded', function(){
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(toggle && nav){
    toggle.addEventListener('click',function(){ nav.classList.toggle('open'); });
  }
  // FAQ 折叠
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      this.parentElement.classList.toggle('open');
    });
  });
});
