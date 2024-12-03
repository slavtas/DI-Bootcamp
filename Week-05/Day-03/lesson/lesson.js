let myObj = {
    name : "John",
    lastName : "Doe",
    age : 25,
    friends : ["Mark", "Lucie", "Ana"]
};
objArr.forEach((entry, index) => {
    console.log(`The ${index+1} key is: ${entry[0]}. The ${index+1} value is ${entry[1]}}`);
});
