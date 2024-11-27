// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the second <li> of the second <ul>.
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.

const containerDiv = document.getElementById("container");
console.log(containerDiv);

const firstList = document.querySelectorAll(".list")[0];
firstList.children[1].textContent = "Richard";

const secondList = document.querySelectorAll(".list")[1];
secondList.children[1].remove();

document.querySelectorAll(".list").forEach((list) => {
    list.children[0].textContent = "Slava";
});

document.querySelectorAll(".list").forEach((list) => {
    list.classList.add("student_list");
});

firstList.classList.add("university", "attendance");

containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

Array.from(secondList.children).forEach((li) => {
    if (li.textContent === "Dan") {
        li.style.display = "none";
    }
});

Array.from(firstList.children).forEach((li) => {
    if (li.textContent === "Richard") {
        li.style.border = "1px solid black";
    }
});

document.body.style.fontSize = "18px";