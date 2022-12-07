const wrapper = document.querySelector('.p-wrapper');
const indicators = [...document.querySelectorAll('.p-indicators button')];

let currentTestimonial = 0; // Default 0

indicators.forEach((item, i) => {
    item.addEventListener('click', () => {
        indicators[currentTestimonial].classList.remove('p-active');
        wrapper.style.marginLeft = `-${100 * i}%`;
        item.classList.add('p-active');
        currentTestimonial = i;
    })
})