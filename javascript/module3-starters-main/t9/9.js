'use strict'

function check(type) {
    let answer;
    if (type[1] === '/') {
        answer = type[0]/type[2]
        return answer
    } else if (type[1] === '+') {
        answer = type[0]+type[2]
        return answer
    } else if (type[1] === '-') {
        answer = type[0]-type[2]
        return answer
    } else if (type[1] === '*') {
        answer = type[0]*type[2]
        return answer
    } else {return false}
}
function split(calc) {
    let num1 = "";
    let num2 = "";
    let type = null;

    for (let ch of calc) {
        if (!type && "+-*/".includes(ch)) {
            type = ch;
        } else if (!type) {
            num1 += ch;
        } else {
            num2 += ch;
        }
    }
    return [Number(num1), type, Number(num2)];
}


function calculate () {
    let calc = document.getElementById("calculation").value

    let luvut = split(calc)

    const answer = check(luvut)

    if (answer !== false) {
        document.getElementById("result").innerHTML = answer
    }
}
