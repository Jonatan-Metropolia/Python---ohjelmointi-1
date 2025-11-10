'use strict';

function concat(array) {
    let string = '';

    for (let value of array) {
        string += value
    }

    return string
}

const array = ["Jonatan", "Pekka", "juu", "moro"]
let connected;
connected = concat(array)

document.querySelector('#concat').innerHTML = connected;
