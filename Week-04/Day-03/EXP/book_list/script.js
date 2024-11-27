// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.

const allBooks = [
    {
        title: "Harry Potter and the Sorcerer's Stone",
        author: "J.K. Rowling",
        image: "https://assets-prd.ignimgs.com/2022/12/13/potterpc-1670965301648.jpg",
        alreadyRead: true,
    },
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        image: "https://www.mayobooks.ie/image/cache/catalog/51g3AS16r9L-1000x1000.jpg",
        alreadyRead: false,
    },
];

const listBooksSection = document.querySelector(".listBooks");

allBooks.forEach((book) => {

    const bookDiv = document.createElement("div");
    bookDiv.classList.add("book");

    const bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.alt = `${book.title} cover`;
    bookImage.style.width = "100px";

    const bookDetails = document.createElement("div");
    bookDetails.classList.add("book-details");
    bookDetails.textContent = `${book.title} written by ${book.author}`;

    if (book.alreadyRead) {
        bookDetails.classList.add("read");
    }

    bookDiv.appendChild(bookImage);
    bookDiv.appendChild(bookDetails);

    listBooksSection.appendChild(bookDiv);
});
