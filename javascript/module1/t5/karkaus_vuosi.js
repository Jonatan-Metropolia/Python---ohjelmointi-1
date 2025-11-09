'use strict';


const input = prompt('Anna vuosi: ');
let leap;


if (input %4 !== 0) {
    leap = false;
} else if (input %100 !== 0 ) {
    leap = true;
} else if (input %400 !== 0) {
    leap = false;
} else {
    leap = true;
}

if (leap === false) {
    document.querySelector('#karkaus').innerHTML = 'Vuosi: ' + input + ' ei ole karkaus vuosi';
} else {
    document.querySelector('#karkaus').innerHTML = 'Vuosi: ' + input + ' on karkaus vuosi';
}