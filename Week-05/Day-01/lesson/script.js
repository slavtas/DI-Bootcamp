// function centuryChecker (year) {
//     year > 2000 ? console.log("You are in the 21st century") : console.log("You are in the Middle Ages")
// }

// centuryChecker(9340);
// centuryChecker(18);

// const calculator = (num1, num2, operator) =>
//     operator === "+" ? num1 + num2 :
//     operator === "-" ? num1 - num2 :
//     operator === "*" ? num1 * num2 :
//     operator === "/" ? (num2 !== 0 ? num1 / num2 : "Cannot divide by zero") : 
//     Invalid operator;

// console.log(calculator(6, 3, "/"));

// const hummus = function(factor) {
//     const ingredient = function(amount, unit, name) {
//         let ingredientAmount = amount * factor;
//         if (ingredientAmount > 1) {
//             unit += "s";
//         }
//         console.log(`${ingredientAmount} ${unit} ${name}`);
//     };
//     ingredient(1, "can", "chickpeas");
//     ingredient(0.25, "cup", "tahini");
//     ingredient(0.25, "cup", "lemon juice");
//     ingredient(1, "clove", "garlic");
//     ingredient(2, "tablespoon", "olive oil");
//     ingredient(0.5, "teaspoon", "cumin");
// };

// hummus(2)


let add = (function () {
    let counter = 0;
    function calculus() {
        counter += 1; 
        return counter
    }
    return calculus
  })();
  
  console.log(add());
  console.log(add());
  console.log(add());