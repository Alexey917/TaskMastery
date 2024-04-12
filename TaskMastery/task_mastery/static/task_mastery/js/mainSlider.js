const mainTaskMastery = document.querySelector(".main-task-mastery");
const section = document.querySelectorAll(".main-section");
const sliderBtnNext = document.querySelector(".slider-btn-next");
const sliderBtnPrev = document.querySelector(".slider-btn-prev");


let counter = 0;
const slider = [];

sliderBtnPrev.classList.add("section-hiden");

function checkSlider() {
  if (counter === section.length - 1) {
    sliderBtnNext.classList.add("section-hiden");
  } else {
    sliderBtnNext.classList.remove("section-hiden");
  }

  if (counter === 0) {
    sliderBtnPrev.classList.add("section-hiden");
  } else {
    sliderBtnPrev.classList.remove("section-hiden");
  }
}

function displaySection() {
  for (let i = 0; i < section.length; i++) {
    i !== counter
      ? section[i].classList.add("section-hiden")
      : section[i].classList.remove("section-hiden");
  }
}

displaySection();

sliderBtnNext.addEventListener("click", () => {
  section[counter].classList.add("disappearence");
  counter++;
  displaySection();
  console.log(counter);
  checkSlider();
});

sliderBtnPrev.addEventListener("click", () => {
  counter--;
  displaySection();
  console.log(counter);
  checkSlider();
});

console.log(counter);
console.log(section.length);
