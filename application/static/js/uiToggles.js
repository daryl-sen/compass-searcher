window.onload = () => {

  const mobileNavButton = document.getElementById('mobile-nav-button');
  const mobileNavMenu = document.getElementById('nav-links');
  const shades = document.getElementById('shades');
  const closeMenuButton = document.getElementById('close-button');
  
  const toggleElement = (id) => {
    target = document.getElementById(id);
    target.classList.toggle('hidden');
  };
  
  const toggleMenu = () => {
    shades.classList.toggle('hidden');
    mobileNavMenu.classList.toggle('display-block')
  }
  
  mobileNavButton.addEventListener('click', toggleMenu);
  shades.addEventListener('click', toggleMenu);
  closeMenuButton.addEventListener('click', toggleMenu);
}