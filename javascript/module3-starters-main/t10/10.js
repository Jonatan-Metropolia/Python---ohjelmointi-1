'use strict';

const form = document.getElementById('source');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const firstname = document.getElementById('firstname').value;
    const lastname = document.getElementById('lastname').value;

    document.getElementById('target').textContent = 'Your name is ' + firstname + ' ' + lastname;
})
