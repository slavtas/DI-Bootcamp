// const obj = require('./main.js')

import {multi,divide,plus,minus} from "./math.js";
// console.log(obj);

// console.log(obj.hello('Dan'));
// console.log(a);

try {
    console.log(multi(2,5));
    console.log(divide(2,5));
    console.log(divide(2,1));
    console.log(plus(2,10));
    console.log(minus(2,8));
} catch (error) {
    console.log(error);
};