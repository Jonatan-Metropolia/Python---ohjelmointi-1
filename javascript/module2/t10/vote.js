'use strict';

const candidates_amount = prompt('Montako osallistujaa?')

let candidates = [];
for (let i = 1; i <= candidates_amount; i++) {
    let name = prompt (`${i}. ehdokas`)
    candidates.push(
        {
        name: name,
        votes: 0,
        },
    )
}


let number_voters = prompt ('Montako äänestäjää?')
number_voters = parseInt(number_voters)
let current_votes;
for (let i = 1; i <= number_voters; i++) {
    let vote = prompt ('Ketä äänestät ( anna nimi )')

    for (let k = 0; k <= candidates.length-1; k++) {
        if (vote === candidates[k].name) {
            current_votes = candidates[k].votes +1;
            console.log('loopissa')
            candidates[k].votes = current_votes;
            break;
        }
    }
}


let winner;
let most_votes = 0;
for (let i = 0; i <= candidates.length - 1;i++) {
    if (candidates[i].votes >= most_votes) {
        most_votes = candidates[i].votes
        winner = candidates[i].name
    }
}


candidates.sort((a, b) =>{
    return b.votes - a.votes;
});

console.log(`Voittaja on ${winner}, ${most_votes} äänellä! \n\n Results:`)
console.log(candidates)
