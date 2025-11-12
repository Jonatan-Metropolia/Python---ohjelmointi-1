'use strict';

const items = ['First', 'Second', 'Third'];
const ul = document.querySelector('#target');

for (let value of items) {
    let text = document.createTextNode(`${value} item`);
    const li = document.createElement("li");

    li.appendChild(text);
    ul.appendChild(li)
}

