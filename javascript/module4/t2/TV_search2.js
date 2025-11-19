'use strict';

async function hae(query) {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`) ;
    const taulukko = await response.json();

    return taulukko;
}


const form = document.querySelector('form');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const query = document.querySelector('#query').value

    const tulos = hae(query)

    console.log(tulos)
})


