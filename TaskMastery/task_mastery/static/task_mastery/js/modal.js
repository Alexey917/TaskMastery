const btnRegistration = document.querySelector(".introductory-section-btn");
const modalRegistration = document.querySelector(".modal-registration");
const btnAuthorization = document.querySelector(".authorization");
const modalAuthorization = document.querySelector(".modal-authorization");
const closeAuthorization = document.querySelector(".btn-close-authorization");
const closeRegistration = document.querySelector(".btn-close-registration");
const dialogRegistration = document.querySelector(".modal-dialog-registration");
const dialogAuthorization = document.querySelector(
  ".modal-dialog-authorization"
);

btnRegistration.addEventListener("click", () =>
  modalRegistration.classList.add("modal-is-open")
);

btnAuthorization.addEventListener("click", () =>
  modalAuthorization.classList.add("modal-is-open")
);

closeAuthorization.addEventListener("click", () =>
  modalAuthorization.classList.remove("modal-is-open")
);

closeRegistration.addEventListener("click", () =>
  modalRegistration.classList.remove("modal-is-open")
);

modalRegistration.addEventListener("click", (event) => {
  const target = event.target;

  if (!target.classList.contains("dialogRegistration")) {
    target.classList.remove("modal-is-open");
  }
});

modalAuthorization.addEventListener("click", (event) => {
  const target = event.target;

  if (!target.classList.contains("dialogAuthorization")) {
    target.classList.remove("modal-is-open");
  }
});

document.addEventListener("keyup", (event) => {
  if (
    event.key == "Escape" &&
    modalRegistration.classList.contains("modal-is-open")
  ) {
    testModal.classList.toggle("modal-is-open");
  }
});

document.addEventListener("keyup", (event) => {
  if (
    event.key == "Escape" &&
    modalAuthorization.classList.contains("modal-is-open")
  ) {
    modalAuthorization.classList.toggle("modal-is-open");
  }
});