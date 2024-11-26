// Part I - Review about arrays
// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that gives the index of “Foo”. Why does it return -1 ?

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

const people = ["Greg", "Mary", "Devon", "James"];

// 1. Remove “Greg” from the people array
people.shift();
console.log(people);

// 2. Replace “James” with “Jason”
people[people.indexOf("James")] = "Jason";
console.log(people);

// 3. Add your name to the end of the people array
people.push("Slava");
console.log(people);

// 4. Log Mary’s index
console.log(people.indexOf("Mary"));

// 5. Copy the array without “Mary” and "YourName" using slice
const newPeople = people.slice(1, people.length - 1); 
console.log(newPeople);

// 6. Find the index of “Foo”
console.log(people.indexOf("Foo"));
// Explanation: "Foo" is not in the array, so `indexOf` returns -1 when the element is not found.

// 7. Create a variable `last` to get the last element of the array
const last = people[people.length - 1];
console.log(last);