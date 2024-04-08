const mainTaskMastery = document.querySelector(".main-task-mastery");
const section = document.querySelectorAll(".main-section");
const sliderBtnNext = document.querySelector(".slider-btn-next");
const sliderBtnPrev = document.querySelector(".slider-btn-prev");

let counter = 0;
const slider = [];

// section.forEach((element) => {
//   slider.push(element);
// });

// mainTaskMastery.innerHTML = section[0];

function displaySection() {
  for (let i = 0; i < section.length; i++) {
    i !== counter
      ? section[i].classList.add("section-hiiden")
      : section[i].classList.remove("section-hiiden");

    console.log(section[i]);
  }
}

displaySection();

sliderBtnNext.addEventListener("click", () => {
  counter++;
  displaySection();
});

sliderBtnPrev.addEventListener("click", () => {
  counter--;
  displaySection();
});

console.log(sliderBtnNext);
