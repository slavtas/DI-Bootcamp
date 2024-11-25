// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.

// one loop solution

const maxNumber = 6;
// for (let i=0; i < maxNumber; i++){
//     console.log(i)
// };
let asterix = ""
// for (let i=0; i < maxNumber; i++){
//     asterix = asterix + "*"
//     console.log(asterix)
// };

// two nested for loops solution

for (let i=0; i < maxNumber; i++){
    const numberOfAsterix = i + 1
    let lineOfAsterix = ""
    for (let j = 0; j < numberOfAsterix; j++){
        lineOfAsterix = lineOfAsterix + "*"
    }
    console.log(lineOfAsterix)
};