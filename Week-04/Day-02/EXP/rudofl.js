// Instructions
// Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'reindeer'
  }

let words = [];

for (let key in details) {
    words.push(key);
    words.push(details[key]);
}

let sentence = words.join(" ");
  
console.log(sentence);