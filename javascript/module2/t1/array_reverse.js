'use strict'

function array_create(len) {
    let array = [];

    for ( let i = 1; i <= 5; i++) {
        let input = prompt('Give ' + i + '. num (out of )' +len)
        array.push(input)
    }

    return array;
}


function array_reverse (array) {
    let reverse = []
    for (let i = array.length - 1; i >=0 ; i--)  {
        reverse.push(array[i])
    }

    return reverse;
}

const len = 5

let array= array_create(len);

const reversed_array = array_reverse(array);

console.log(reversed_array);

