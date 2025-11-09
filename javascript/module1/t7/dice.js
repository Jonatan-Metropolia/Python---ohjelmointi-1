'use strict';

const sides = prompt('Enter the number of sides on the dice');
const throws = prompt('Number of dice rolls: ');

let sum = 0;

for (let i = 1; i <= throws; i++) {
    sum += Math.floor(Math.random() * sides +1)
}

document.querySelector('#dice').innerHTML = 'Noppien summa = ' + sum;
