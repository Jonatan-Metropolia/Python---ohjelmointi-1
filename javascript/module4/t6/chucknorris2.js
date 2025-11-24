'use strict';

async function fetch_joke(query) {
    const url = `https://api.chucknorris.io/jokes/search?query=${query}`;
    const result = await fetch(url);
    const json = await result.json();
    return json.result[0].value;
}
const nappi = document.getElementById("nappi");

nappi.addEventListener('click', async () => {
    const query = document.querySelector("#query").value;
    const joke = await fetch_joke(query);

    const body = document.querySelector('body')
    const article = document.createElement('article');
    const p = document.createElement('p');

    const text = document.createTextNode(`${joke}`);

    p.appendChild(text);
    article.appendChild(p);
    body.appendChild(article)
})
