'use strict';

const array = [2, 9, 4, 11];

function even(array) {
    let even_array = [];

    for (let value of array) {
      if (value %2 === 0) {
          even_array.push(value)
      }
    }

    return even_array;
}

const sorted = even(array)

console.log(array, sorted)