'use strict';

let start = prompt('Start year');
let end = prompt ('End year');


end = parseInt(end);
start = parseInt(start);

if (start > end) {
let placeholder = start;
start = end;
end = placeholder;
}



let leap;
let html = ``;
for (let i = start; i <= end; i++) {


    if (i % 4 !== 0) {
        leap = false;
    } else if (i % 100 !== 0) {
        leap = true
    } else if (i % 400 !==0) {
        leap = false
    } else {
        leap = true
    }

    if (leap === true) {
        html += `<li>${i}</li>`;
    }
}
const element = document.querySelector('#leep');
element.innerHTML = html
