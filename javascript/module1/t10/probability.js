'use strict';



function dice_throw(n, t, tries) {
    let sum = 0;
    let target_amount = 0;

    for (let i = 1; i <= tries; i++) {
        for (let k = 1; k <= n; k++) {
            sum += Math.floor(Math.random() * 6 + 1);
        }

        if (sum === t) {target_amount++}
        sum = 0;
    }
    return target_amount
}


function probability (n, t) {
    if (n * 6 < t || t < n) {
        alert('Virhe syötteessä!')
        return;
    }

    const tries = 10000;
    const target_reached = dice_throw(n, t, tries);
    return (target_reached / tries) * 100;
}

function decimal(value) {
    return Number.parseFloat(value).toFixed(2);
}

/* ------    main    ----- */
let num_of_throws = prompt('Montako noppaa haluat heittää?')
let target = prompt('Minkä luvun haluat saada summana?')

num_of_throws = parseInt(num_of_throws);
target = parseInt(target);


const prob = probability(num_of_throws, target)

const element = document.querySelector('#probability')
element.innerHTML = 'Probability to get sum '+ target+ ' with '+ num_of_throws+ ' throws = ' + decimal(prob)+ '%'

