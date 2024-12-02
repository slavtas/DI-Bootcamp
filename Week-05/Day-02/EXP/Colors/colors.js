// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")

// Exercise_1

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach((color, index) => {
    console.log(`${index +1}# choice is ${color}.`);
});

// Option_1

if (colors.includes("Violet")) {
    console.log("Yeah");}
    else {
        console.log("Nope");
    };

// Option_2

const equalViolet = colors.some(color => color === "Violet");
console.log(equalViolet ? "Yep" : "Nope");

// Exercise_2
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…

const ordinal = ["th","st","nd","rd"];

colors.forEach((color, index) => {
    const position = index +1;
    const suffix = position === 1 ? ordinal [1]
    : position === 2 ? ordinal [2]
    : position === 3 ? ordinal [3]
    : ordinal [0];
    console.log(`${position}${suffix} choice is ${color}.`)
});


    