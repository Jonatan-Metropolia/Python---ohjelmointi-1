'use strict';

async function hae(query) {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`) ;
    return await response.json();
}


function print_to_page(list) {

    const div = document.getElementById('results');
    div.innerHTML = "";
    for (let value of list) {

        const article = document.createElement('article');
        const h2 = document.createElement('h2');
        const a = document.createElement('a');
        const p = document.createElement('p');
        const img = document.createElement('img');

        h2.textContent = value.show.name;

        a.href = value.show.url;
        a.target = "_blank";
        a.textContent = value.show.url;

        p.innerHTML = value.show.summary || "No summary availible";

        img.src = value.show.image?.medium;
        img.alt = value.show.name;


        article.appendChild(h2);
        article.appendChild(a);
        article.appendChild(p);
        article.appendChild(img);

        div.appendChild(article);
    }
}

const form = document.querySelector('form');

form.addEventListener('submit', async function(e) {
    e.preventDefault();

    const query = document.querySelector('#query').value;

    const tulos = await hae(query);
    print_to_page(tulos);
});



