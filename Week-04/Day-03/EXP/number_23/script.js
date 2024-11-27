// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.

// Bonus: Add a parameter divisor to the function.

// displayNumbersDivisible(divisor)
// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
// and their sum

function displayNumbersDivisible(divisor) {
    let sum = 0;
    for (let i = 0; i<500;i++) {
        if(i%divisor === 0) {
            console.log(i);
            sum+= i;
        }
    }
    console.log("Sum: ", sum);
}
displayNumbersDivisible(23);
displayNumbersDivisible(3);
displayNumbersDivisible(45);