'use strict';

const name = prompt('Anna nimesi');
const random = Math.floor(Math.random()*4);
let talo;

if (random === 0) {
    talo = 'Gryffindor'
}
else if (random === 1) {
    talo = 'Hufflepuff'
}
else if (random === 2) {
    talo = 'Ravenclaw'
}
else if ( random === 3) {
    talo = 'Slytherin'
}

document.querySelector('#hattu').innerHTML = name + ', sinun talosi on: ' + talo;