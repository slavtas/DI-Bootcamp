// console.log('my first nodejs file');

// let arr = [1,2,3]
// arr.map(item => {
//     console.log(item);
// })


const hello = (name) => {
    return `Hello, ${name}, welcome to NodeJS`
}
// console.log(hello ('John'));

const greeting = (name) => {
    return `hello ${name}`
}

let a = 10;
let b = 5;

module.exports = {
    hello,
    a,
    greeting,
};