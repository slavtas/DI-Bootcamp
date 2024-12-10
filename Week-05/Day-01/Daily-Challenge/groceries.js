// Using this object :

let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}
// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};
displayGroceries();

// Create another arrow function named cloneGroceries.
const cloneGroceries = () => {
// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
// Change the client variable to “Betty”. 'user' holds a copy of the original string, therefore changing 'client' to 'Betty' does not affect 'user' 
    let user = client;
    client = "Betty";
// In the function, create a variable named shopping that is equal to the groceries variable.
    let shopping = groceries;
// Change the value of the totalPrice key to 35$. Change the value of the paid key to false. 'groceries' and 'shopping' point to the same memory reference, modifications in 'shopping' object will be reflected in 'groceries'
    shopping.totalPrice = "35$";
    shopping.other.paid = false;

    console.log(`Client: ${client}`);  // Output: Betty
    console.log(`User: ${user}`);      // Output: John
    console.log(`Shopping totalPrice: ${shopping.totalPrice}`); // Output: 35$
    console.log(`Groceries totalPrice: ${groceries.totalPrice}`); // Output: 35$
    console.log(`Groceries paid: ${groceries.other.paid}`); // Output: false
};
// Invoke the cloneGroceries function.
cloneGroceries();