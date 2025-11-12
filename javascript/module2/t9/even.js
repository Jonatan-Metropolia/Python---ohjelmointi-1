'use strict';

function even(array) {
    let even_array = [];

    for (let i = 0; i <= array.length -1; i++) {
        let value = array[i];
        if (value %2 === 0) {
            even_array.push(value)
        }
    }

    return even_array;
}
const array = [1, 8, 9, 5, 33, 9808];

const even_array = even(array)
console.log(even_array)

