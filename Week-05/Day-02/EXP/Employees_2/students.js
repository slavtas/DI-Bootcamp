// Using the filter() method, create a new array, 
// containing the students that passed the course.
// Bonus : Chain the filter method with a forEach method, 
// to congratulate the students with their name and course name 
// (ie. “Good job Jenner, you passed the course in Information Technology”, 
// “Good Job Marco you passed the course in Robotics” ect…)

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
    {name: "Liam", course: "Computer Science", isPassed: false}, 
    {name: "Jenner", course: "Information Technology", isPassed: true}, 
    {name: "Marco", course: "Robotics", isPassed: true}, 
    {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
    {name: "Jamie", course: "Big Data", isPassed: false}];

const winners = students.filter(student => student.isPassed === true);
console.log(winners);

students.filter(student => student.isPassed === true)
.forEach(student => console.log(`Well done ${student.name}, you earned a cookie for passing the ${student.course} course.`)); 