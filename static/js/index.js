// JavaScript to trigger the sliding effect
window.addEventListener('load', function() {
    document.querySelector('.text-box').classList.add('slide-in-left');
    document.querySelector('.image-box').classList.add('slide-in-right');
});
document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('#container input[type="radio"]');
    let currentIndex = 0;
    const slideInterval = setInterval(nextSlide, 4000);

    function nextSlide() {
        slides[currentIndex].checked = false;
        currentIndex = (currentIndex + 1) % slides.length;
        slides[currentIndex].checked = true;
    }
});
