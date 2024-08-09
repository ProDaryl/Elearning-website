document.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.header .menu');
    const navUl = document.querySelector('.header nav ul');
  
    menu.addEventListener('click', () => {
      navUl.classList.toggle('show');
    });
  });
  