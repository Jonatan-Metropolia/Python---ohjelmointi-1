'use strict';

function list_create(amount) {
    let list = [];

    for (let i = 1; i <= amount; i++) {
        let name = prompt('Anna ' + i + '. nimi')
        list.push(name);
    }
    return list;
}


function print_list(list) {

    let html=``;
    for (let i = 0; i <= list.length-1; i++){
        html += `<li>${list[i]}</li>`
    }

    document.querySelector('#list').innerHTML = html;

}

const amount = prompt('Number of guests: ')

const member_list = list_create(amount);

member_list.sort()

print_list(member_list);



