'use strict';

function dice_roll (sides) {
    let value= Math.floor(Math.random() * sides) + 1;
    return value;
}


let html = ``
let dice = 0;
const sides = parseInt(prompt('Montako sivua nopassa?'))

while (dice !== sides) {
    dice = dice_roll(sides);
    html += `<li>${dice}</li>`;
}

document.querySelector('#dice').innerHTML = html;
