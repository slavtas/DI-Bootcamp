// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".

let user = {
    username : 'billythekid',
    password : 'password'
}

const database = [user]

let newsfeed = [
    {username: user.username, timeline: ['clicked', 'button pushed', 'form submitted']}, 
    {username: 'timmy', timeline: ['messaged', 'joined']}, 
    {username: 'floyd', timeline: []}
];

console.log(newsfeed)