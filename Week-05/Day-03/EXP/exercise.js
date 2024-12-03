// ------- Exercise_1 -------

// Analyze the code below. What will be the output?
// Expected output --> person = {name:'John Doe', age:25, location {country:'Canada', city:'Vancouver', coordinates:[49.2827, -123.1207]}}
// "I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)"

// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;
// console.log(person);
// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// ------- Exercise_2 -------

// Using the code, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'

// function displayStudentInfo(objUser){
//     const {first, last} = objUser;
//     console.log(`Your full name is ${objUser.first} ${objUser.last}`);
// };

// displayStudentInfo({first: 'Elie', last:'Schoppik'});

// ------- Exercise_3 -------

// Using this object 

// const users = { user1: 18273, user2: 92833, user3: 90315 };

// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.

// const usersArray = Object.entries(users);
// console.log(usersArray);

// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]

// const updUsersArray = usersArray.map(([key, value]) => [key, value * 2]);
// console.log(updUsersArray);

// ------- Exercise_4 -------

// Analyze the code below. What will be the output?

// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
  
//   const member = new Person('John');
//   console.log(typeof member);

// Output --> object

// ------- Exercise_5 -------

// Using the Dog class below:

// class Dog {
//   constructor(name) {
//     this.name = name;
//   }
// };
// Analyze the options below. Which constructor will successfully extend the Dog class?
  // 1
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.size = size;
//   }
// };


  // 2 THE ONLY RIGHT OPTION

// class Labrador extends Dog {
//   constructor(name, size) {
//     super(name);
//     this.size = size;
//   }
// };


  // 3
// class Labrador extends Dog {
//   constructor(size) {
//     super(name);
//     this.size = size;
//   }
// };


  // 4
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.name = name;
//     this.size = size;
//   }
// };

// ------- Exercise_6 -------

// Evaluate these (ie True or False)

// [2] === [2] // False, arrays are objects, and objects are compared by reference and not their values
// {} === {}   // False, objects don not have the same reference

// What is, for each object below, the value of the property number and why?

// const object1 = { number: 5 }; 
// const object2 = object1;         // 5, because obj2 references obj 1, i.e. points at the same memory location
// const object3 = object2;         // 5, same story, obj3 --> obj2 --> obj1 --> 5
// const object4 = { number: 5};    // 5, but separate from obj1, obj2 and obj3, because it's a new object in new memory location

// object1.number = 4;          // all objects that reference obj1 will see and share the change, obj4 stays the same
// console.log(object2.number)
// console.log(object3.number)
// console.log(object4.number)

// Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin etc …
class Animal {
    constructor(name, type, color) {
        this.name = name,
        this.type = type,
        this.color = color
    };
};
// Create a class Mammal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.
class Mammal extends Animal {
    constructor(name, type, color, sound) {
        super(name, type, color);
        this.sound = sound;
    };
speak() {
    console.log(`${this.sound}! I am a ${this.type}, my name is ${this.name} and I'm ${this.color}.`)
}};
// Create a farmerCow object that is an instance of the class Mammal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
let farmerCow = new Mammal('Lily', 'cow', 'brown and white', 'Mooo');
farmerCow.speak();
// For example: Moooo I'm a cow, named Lily and I'm brown and white