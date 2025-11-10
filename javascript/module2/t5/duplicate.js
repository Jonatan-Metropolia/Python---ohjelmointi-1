'use strict';

let nums = []
let main_loop = true;
while (main_loop === true) {
    let num = prompt('Anna luku')
    num = parseInt(num)

    if (!nums.includes(num)) {
        nums.push(num);
    } else {
        alert('Numero on jo annettu!')
        main_loop = false;
    }
}

nums.sort()

for(let i = nums.length-1; i >= 0; i--) {
    console.log(nums[i])
}