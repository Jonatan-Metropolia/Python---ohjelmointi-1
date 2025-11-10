'use strict';

function dice_roll () {
    let value= Math.floor(Math.random() * 6) + 1;
    return value;
}


let html = ``
let dice = 0;
while (dice !== 6) {
    dice = dice_roll();
    html += `<li>${dice}</li>`;
}

document.querySelector('#dice').innerHTML = html;
