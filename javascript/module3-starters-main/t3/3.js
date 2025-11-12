'use strict';
const names = ['John', 'Paul', 'Jones'];

const ul = document.querySelector('#target');

for (let value of names) {
    const li = document.createElement('li')
    const text = document.createTextNode(value)

    li.appendChild(text)
    ul.appendChild(li)
}

