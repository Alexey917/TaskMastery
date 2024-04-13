const btnRegistration = document.querySelector(".introductory-section-btn");
const modalRegistration = document.querySelector(".modal-registration");
const btnAuthorization = document.querySelector(".authorization");
const modalAuthorization = document.querySelector(".modal-authorization");

btnRegistration.addEventListener("click", () =>
  modalRegistration.classList.add("modal-is-open")
);

btnAuthorization.addEventListener("click", () =>
  modalAuthorization.classList.add("modal-is-open")
);
