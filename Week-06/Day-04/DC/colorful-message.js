async function displayMessage() {
    const chalk = (await import('chalk')).default;
    console.log(chalk.green("This is a colorful message!"));
};

module.exports = {displayMessage};