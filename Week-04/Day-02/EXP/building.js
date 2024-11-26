// Instructions:
// Review about objects
// Copy and paste the above object to your Javascript file.
// Console.log the number of floors in the building.
// Console.log how many apartments are on the floors 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
// 1.
console.log(`Number of floors in the building: ${building.numberOfFloors}`);
// 2.
console.log(`Number of apartments on the 1st floor: ${building.numberOfAptByFloor.firstFloor}`);
console.log(`Number of apartments on the 3rd floor: ${building.numberOfAptByFloor.thirdFloor}`);
// 3.
const secondTenant = building.nameOfTenants[1];
const secondTenantRooms = building.numberOfRoomsAndRent.dan[0];
console.log(`The second tenant is ${secondTenant} and he has ${secondTenantRooms} rooms.`);
// 4.
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent was increased to 1200.");
} else {
    console.log("Dan's rent remains the same.");
}

console.log(building.numberOfRoomsAndRent);