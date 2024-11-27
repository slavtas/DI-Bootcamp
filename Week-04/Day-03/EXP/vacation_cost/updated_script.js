// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

function hotelCost(nights) {
    const costPerNight = 140;
    return nights * costPerNight;
}

function planeRideCost(destination) {
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

function rentalCarCost(days) {
    const costPerDay = 40;
    let totalCost = days * costPerDay;

    if (days > 10) {
        totalCost *= 0.95; // Apply a 5% discount
    }
    return totalCost;
}

function totalVacationCost() {

    let nights, destination, days;

    do {
        nights = prompt("How many nights would you like to stay in the hotel?");
        nights = parseInt(nights);
    } while (isNaN(nights) || nights <= 0);

    do {
        destination = prompt("What is your destination?");
    } while (!destination || typeof destination !== "string" || destination.trim() === "");

    do {
        days = prompt("How many days would you like to rent the car?");
        days = parseInt(days);
    } while (isNaN(days) || days <= 0);

    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);

    const total = hotel + plane + car;
    console.log(`The car cost: $${car.toFixed(2)}, the hotel cost: $${hotel.toFixed(2)}, the plane tickets cost: $${plane.toFixed(2)}.`);
    console.log(`Total vacation cost: $${total.toFixed(2)}`);
    return total;
}

totalVacationCost();