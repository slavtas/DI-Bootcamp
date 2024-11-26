// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let number = prompt("Enter a number:");

while (Number(number) < 10) {
  number = prompt("The number is less than 10. Please enter a new number:");
}
console.log(`You entered ${number}, which is 10 or greater. Thank you!`);