// const slugify = require('slugify')

// console.log(slugify('my link to the article', '_'));

import { getUsers } from "./info.js";

getUsers('https://jsonplaceholder.typicode.com/users').then((data) => {
    console.log(data);
})