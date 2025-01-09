const greet = require("./greeting");
const colorMessage = require("./colorful-message");
const readFile = require("./read-file");

const userName = "Michael Scott";

greet.greet(userName);
colorMessage.displayMessage();
readFile.readFile();