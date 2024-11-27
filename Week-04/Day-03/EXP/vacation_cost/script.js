// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

function hotelCost() {
    let nights;
    do {
        nights = prompt("How many nights would you like to stay in the hotel?");
        nights = parseInt(nights);
    } while (isNaN(nights) || nights <= 0);

    const costPerNight = 140;
    return nights * costPerNight;
}

function planeRideCost() {
    let destination;
    do {
        destination = prompt("What is your destination?");
    } while (!destination || typeof destination !== "string" || destination.trim() === "");

    destination = destination.toLowerCase().trim();
    switch (destination) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    }
}

function rentalCarCost() {
    let days;
    do {
        days = prompt("How many days would you like to rent the car?");
        days = parseInt(days);
    } while (isNaN(days) || days <= 0);

    const costPerDay = 40;
    let totalCost = days * costPerDay;

    if (days > 10) {
        totalCost *= 0.95; // Apply a 5% discount
    }
    return totalCost;
}

function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();

    const total = hotel + plane + car;
    console.log(`The car cost: $${car.toFixed(2)}, the hotel cost: $${hotel.toFixed(2)}, the plane tickets cost: $${plane.toFixed(2)}.`);
    console.log(`Total vacation cost: $${total.toFixed(2)}`);
    return total;
}

totalVacationCost();