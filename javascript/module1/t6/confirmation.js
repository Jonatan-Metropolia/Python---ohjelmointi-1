'use strict';

const answer = confirm('Lasketaanko neliöjuuri?');

if (answer) {
    const num = prompt('Anna luku');

    const numInt = parseInt(num);

    const square = Math.sqrt(numInt);

    document.querySelector('#confirmation').innerHTML = 'Squareroot of ' + num + ' = ' + square;
}
