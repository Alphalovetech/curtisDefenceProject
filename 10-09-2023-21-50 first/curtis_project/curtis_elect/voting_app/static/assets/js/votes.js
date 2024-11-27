

const slidepage = document.querySelector("slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");
const progressText = document.querySelector(".step p");
const progressCheck = document.querySelector(".step .check");
const bullet = document.querySelector(".step .bullet");
let current = 1

nextBtnFirst.addEventListener('click', function(event)  {
    event.preventDefault();
    slidepage.style.marginLeft = "-25%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
})  

nextBtnSec.addEventListener("click", function(event){
    event.preventDefault();
    slidepage.style.marginLeft = "-50%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
})

nextBtnThird.addEventListener("click", function(event){
    event.preventDefault();
    slidepage.style.marginLeft = "-75%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
})

submitBtn.addEventListener("click", function(event){
    
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
    setTimeout(function(){
        alert('Your vote was successful');
        location.reload();
    }, 800);
});

prevBtnSec.addEventListener("click", function(event){
    event.preventDefault();
    slidepage.style.marginLeft = "0%";
    bullet[current - 2].classList.add("active");
    progressCheck[current - 2].classList.add("active");
    progressText[current - 2].classList.add("active");
    current -= 1;
})

prevBtnThird.addEventListener("click", function(event){
    event.preventDefault();
    slidepage.style.marginLeft = "-25%";
    bullet[current - 2].classList.add("active");
    progressCheck[current - 2].classList.add("active");
    progressText[current - 2].classList.add("active");
    current -= 1;
})

prevBtnFourth.addEventListener("click", function(event){
    event.preventDefault();
    slidepage.style.marginLeft = "-50%";
    bullet[current - 2].classList.add("active");
    progressCheck[current - 2].classList.add("active");
    progressText[current - 2].classList.add("active");
    current -= 1;
})
