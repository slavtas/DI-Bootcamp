// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    father: "Homer",
    mother: "Marge",
    son: "Bart",
    daughter: "Lisa",
};

console.log("Keys of the family object:");
for (let key in family) {
    console.log(key);
}

console.log("Values of the family object:");
for (let key in family) {
    console.log(family[key]);
}