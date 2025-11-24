'use strict';

async function fetch_joke() {
    const result = await fetch("https://api.chucknorris.io/jokes/random");
    const json = await result.json();
    return json.value;
}

const nappi = document.querySelector('#nappi')

nappi.addEventListener('click', async() => {
    const tulos = await fetch_joke();
    console.log(tulos);
});