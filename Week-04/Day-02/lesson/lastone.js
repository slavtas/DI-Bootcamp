// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

let names= ["john", "sarah", 23, "Rudolf",34]

// for (name in names) {
//     if (typeof name == "string") {
//         if (! names.charAt(0).toUpperCase() === name.charAt(0)) {
//            let upperedName = names.charAt(0).toUpperCase() + name.slice(1)
//            names [name] = upperedName;
//         }
//     }
// }




for (let i = 0; i < names.length; i++) {
    let item = names[i];
    if (typeof item === "string") {
        if (item[0] !== item[0].toUpperCase()) {
            item = item[0].toUpperCase() + item.slice(1);
        }
        console.log(item);
    }
}

console.log(names);