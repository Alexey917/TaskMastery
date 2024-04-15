const btnAuthorization = document.querySelector(".authorization");
const modalAuthorization = document.querySelector(".modal-authorization");
const closeAuthorization = document.querySelector(".btn-close-authorization");
const dialogAuthorization = document.querySelector(
  ".modal-dialog-authorization"
);

btnAuthorization.addEventListener("click", () =>
  modalAuthorization.classList.add("modal-is-open")
);

closeAuthorization.addEventListener("click", () =>
  modalAuthorization.classList.remove("modal-is-open")
);

modalAuthorization.addEventListener("click", (event) => {
  const target = event.target;

  if (!target.classList.contains("dialogAuthorization")) {
    target.classList.remove("modal-is-open");
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
