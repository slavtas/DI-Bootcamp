// Instructions
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let firstLetters = names.map(name => name[0]);

firstLetters.sort();

let secretSocietyName = firstLetters.join('');

console.log(secretSocietyName);