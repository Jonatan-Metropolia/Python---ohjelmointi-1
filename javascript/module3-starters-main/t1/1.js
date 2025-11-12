'use strict';

const items = ['First', 'Second', 'Third'];

let html = ``
for (let value of items) {
    html += `<li>${value} item</li>`
}

document.querySelector('#target').innerHTML = html;
