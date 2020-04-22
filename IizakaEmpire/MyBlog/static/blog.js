var circle = document.querySelector('.material-btn');
var link = document.querySelector('.material-content').querySelectorAll('li');
var ham = document.querySelector('.material-hamburger');
var win = window;

function openMenu(event) {
 
  circle.classList.toggle('active');
  ham.classList.toggle('material-close');
  for (var i = 0; i < link.length; i++) {
    link[i].classList.toggle('active');
  }
  event.preventDefault();
  event.stopImmediatePropagation();
}

function closeMenu() {
  if (circle.classList.contains('active')) {
    circle.classList.remove('active');
    for (var i = 0; i < link.length; i++) {
      link[i].classList.toggle('active');
    }
    ham.classList.remove('material-close');
  }
}

circle.addEventListener('click', openMenu, false);

win.addEventListener('click', closeMenu, false);