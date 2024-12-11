export const multi = (a,b) => {
    return a * b;
};

export const divide = (a,b) => {
    if (b === 0) {
        throw new Error("Division by zero not allowed");
    }
    return a / b;
};

export const plus = (a,b) => {
    return a + b;
};

export const minus = (a,b) => {
    return a - b;
};

// module.exports = {
//     multi,
//     divide,
//     plus,
//     minus,
// };

