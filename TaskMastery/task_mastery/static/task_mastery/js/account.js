document.addEventListener("mousemove", (e) => {
  Object.assign(document.documentElement, {
    style: `
      --move-x: ${(e.clientX - window.innerWidth / 2) * -0.005}deg;
      --move-y: ${(e.clientY - window.innerHeight / 2) * -0.015}deg;
    `,
  });
});

const btnMenu = document.querySelector(".btn-menu");
const navbar = document.querySelector(".navbar");

btnMenu.addEventListener("click", () => {
  navbar.classList.toggle("navbar-open");
  btnMenu.classList.toggle("btn-menu-rotate");
});
