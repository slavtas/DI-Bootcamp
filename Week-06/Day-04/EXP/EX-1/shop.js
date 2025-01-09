const {products} = require("./products");

function findProduct(name) {
  const product = products.find(
    (p) => p.name.toLowerCase() === name.toLowerCase()
  );
  if (product) {
    console.log(
      `Product found: ${product.name}, Price: $${product.price}, Category: ${product.category}`
    );
  } else {
    console.log(`Product "${name}" not found.`);
  }
}

findProduct("Laptop");
findProduct("Hoodie");
findProduct("Coffee Mug");
findProduct("Yoga Mat");
findProduct("Headphones");