const mainTaskMastery = document.querySelector(".main-task-mastery");
const section = document.querySelectorAll(".main-section");
const sliderBtnNext = document.querySelector(".slider-btn-next");
const sliderBtnPrev = document.querySelector(".slider-btn-prev");


let counter = 0;
const slider = [];

sliderBtnPrev.classList.add("section-hidden");

function checkSlider() {
  if (counter === section.length - 1) {
    sliderBtnNext.classList.add("section-hidden");
  } else {
    sliderBtnNext.classList.remove("section-hidden");
  }

  if (counter === 0) {
    sliderBtnPrev.classList.add("section-hidden");
  } else {
    sliderBtnPrev.classList.remove("section-hidden");
  }
}

function displaySection() {
  for (let i = 0; i < section.length; i++) {
    if (i !== counter) {
      section[i].classList.add("disapearence");
      section[i].classList.remove("appearence");
    } else {
      section[i].classList.add("appearence");
      section[i].classList.remove("disapearence");
    }
  }
}

displaySection();

sliderBtnNext.addEventListener("click", () => {
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
