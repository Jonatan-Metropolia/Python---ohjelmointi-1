'use strict';

let num = 1;
let nums = [];
while (num !== 0) {
    num = prompt('Anna numero (0 pysäyttää)')
    num = parseInt(num)
        if (num === 0) {break}

    nums.push(num);

}

nums.sort()

for (let n of nums){
    console.log(n)
}
