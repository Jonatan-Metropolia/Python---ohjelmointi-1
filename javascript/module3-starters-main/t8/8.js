'use stict';

function Calculate() {
    const type = document.getElementById("operation").value;

    const num1 = parseInt(document.getElementById("num1").value)
    const num2 = parseInt(document.getElementById("num2").value)
    let answer;

    if (type === "add") {
        answer = num1+num2
    } else if (type === "sub") {
        answer = num1-num2
    } else if ( type === "multi") {
        answer = num1*num2
    } else if (type === "div") {
        answer = num1/num2
    }

    document.getElementById("result").innerHTML = answer
}