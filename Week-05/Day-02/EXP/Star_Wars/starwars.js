// Use the reduce() method to combine all of these into a single string.

const words = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

const epic = words.reduce((accumulator, currentWord) => `${accumulator} ${currentWord}`);
console.log(epic)