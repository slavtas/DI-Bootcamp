// Analyze these pieces of code before executing them. What will be the outputs ?

// ------1------

// Spread operator will unpack elements of the arrays into single-level array
// Expected output --> ['bread', 'carrots', 'potato', 'chicken', 'apple', 'orange'] 

// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// ------2------

// Spread operator breaks the string into individual characters
// Expected output --> ["U","S","A"]

// const country = "USA";
// console.log([...country]);

// ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);

// An array with two empty slots will be created, no values are given, thus 'undefined'
// Expected output --> [undefined, undefined]