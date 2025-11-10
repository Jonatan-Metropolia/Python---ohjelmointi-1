'use strict';

let dogs = [];

for (let i = 1; i <= 6; i++) {
    let dog = prompt('Anna nimi' + i+ '/'+ 6)
    dogs.push(dog)
}

dogs.sort()

let dogs_sorted_reverse = [];
for (let i = 6-1; i >= 0; i--) {
    dogs_sorted_reverse.push(dogs[i])
}
console.log(dogs_sorted_reverse)
console.log(dogs)

let html = ``
for (let value of dogs_sorted_reverse) {
    html += `<li>${value}</li>`;
}

document.querySelector('#list').innerHTML = html;

