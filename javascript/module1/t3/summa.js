'use strict';
const num1 = prompt('Anna eka luku');
const num2 = prompt('Anna toinen luku');
const num3 = prompt('Anna kolmas luku');

const intnum1 = parseInt(num1);
const intnum2 = parseInt(num2);
const intnum3 = parseInt(num3);

const sum = intnum1 + intnum2 + intnum3;
const product = intnum1 * intnum2 * intnum3;
const avg = sum/3;

document.querySelector('#summa').innerHTML = sum;
document.querySelector('#kerto').innerHTML = product;
document.querySelector('#avg').innerHTML = avg;


