'use strict';

const trigger = document.querySelector('#trigger');
const img = document.querySelector('#target')

trigger.addEventListener('mouseenter', () => {
    img.src = "img/picB.jpg"
});
trigger.addEventListener('mouseleave', () => {
    img.src = "img/picA.jpg"
})
