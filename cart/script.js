// PRODUCTS DATA

const products = [
  {
    id: 1,
    name: "Carton of Grapes",
    price: 4,
    image: "images/Grape.jpg",
  },

  {
    id: 2,
    name: "Bag of Apples",
    price: 10,
    image: "images/Apple.jpg",
  },
  {
    id: 3,
    name: "Carton of Strawberries",
    price: 5,
    image: "images/Strawberry.jpg",
  },
];

// CART

let cart = [];

// APP CONTAINER

const app = document.createElement("div");
app.className = "app";

document.body.appendChild(app);

// TITLE

const title = document.createElement("h1");
title.innerText = "Laith's Fruit Stand";

app.appendChild(title);

// MAIN LAYOUT

const layout = document.createElement("div");
layout.className = "layout";

app.appendChild(layout);

// LEFT SIDE

const leftSide = document.createElement("div");

layout.appendChild(leftSide);

// PRODUCTS TITLE

const productsTitle = document.createElement("h2");
productsTitle.innerText = "Products";

leftSide.appendChild(productsTitle);

// PRODUCTS CONTAINER

const productsContainer = document.createElement("div");
productsContainer.className = "products";

leftSide.appendChild(productsContainer);

// DISPLAY PRODUCTS

products.forEach((product) => {
  const card = document.createElement("div");
  card.className = "card";

  // image
  const image = document.createElement("img");
  image.src = product.image;

  // name
  const name = document.createElement("h3");
  name.innerText = product.name;

  // price
  const price = document.createElement("p");
  price.innerText = `price: $${product.price}`;

  // button
  const button = document.createElement("button");
  button.innerText = "ADD TO CART";

  button.addEventListener("click", () => {
    addToCart(product.id);
  });

  // append
  card.appendChild(image);
  card.appendChild(name);
  card.appendChild(price);
  card.appendChild(button);

  productsContainer.appendChild(card);
});

// CART TITLE

const cartTitle = document.createElement("h2");
cartTitle.innerText = "Your Shopping Cart";

leftSide.appendChild(cartTitle);

// CART CONTAINER

const cartContainer = document.createElement("div");
cartContainer.className = "cart-container";

leftSide.appendChild(cartContainer);

// CHECKOUT

const checkout = document.createElement("div");
checkout.className = "checkout";

layout.appendChild(checkout);

// CHECKOUT TITLE

const checkoutTitle = document.createElement("h2");
checkoutTitle.innerText = "Checkout";

checkout.appendChild(checkoutTitle);

// TOTAL

const totalText = document.createElement("p");
totalText.innerText = "Cart Total: $0";

checkout.appendChild(totalText);

// INPUT

const input = document.createElement("input");
input.type = "number";
input.placeholder = "Enter Cash";

checkout.appendChild(input);

// BUTTON

const submitBtn = document.createElement("button");
submitBtn.innerText = "SUBMIT";

checkout.appendChild(submitBtn);

// RECEIPT

const receipt = document.createElement("div");
receipt.className = "receipt";

checkout.appendChild(receipt);

// ADD TO CART

function addToCart(id) {
  const product = cart.find((item) => item.id === id);

  if (product) {
    product.quantity++;
  } else {
    const item = products.find((p) => p.id === id);

    cart.push({
      ...item,
      quantity: 1,
    });
  }

  renderCart();
}

// RENDER CART

function renderCart() {
  cartContainer.innerHTML = "";

  let total = 0;

  cart.forEach((item) => {
    total += item.price * item.quantity;

    // cart card
    const card = document.createElement("div");
    card.className = "cart-card";

    // name
    const name = document.createElement("h3");
    name.innerText = item.name;

    // price
    const price = document.createElement("p");
    price.innerText = `price: $${item.price}`;

    // quantity
    const quantity = document.createElement("p");
    quantity.innerText = `quantity: ${item.quantity}`;

    // total
    const itemTotal = document.createElement("p");
    itemTotal.innerText = `total: $${item.price * item.quantity}`;

    // plus
    const plus = document.createElement("button");
    plus.innerText = "+";

    plus.addEventListener("click", () => {
      item.quantity++;
      renderCart();
    });

    // minus
    const minus = document.createElement("button");
    minus.innerText = "-";

    minus.addEventListener("click", () => {
      item.quantity--;

      if (item.quantity <= 0) {
        cart = cart.filter((product) => product.id !== item.id);
      }

      renderCart();
    });

    // remove
    const remove = document.createElement("button");
    remove.innerText = "REMOVE";

    remove.addEventListener("click", () => {
      cart = cart.filter((product) => product.id !== item.id);

      renderCart();
    });

    // append
    card.appendChild(name);
    card.appendChild(price);
    card.appendChild(quantity);
    card.appendChild(itemTotal);
    card.appendChild(plus);
    card.appendChild(minus);
    card.appendChild(remove);

    cartContainer.appendChild(card);
  });

  totalText.innerText = `Cart Total: $${total}`;
}

// CHECKOUT

submitBtn.addEventListener("click", () => {
  const total = cart.reduce((sum, item) => {
    return sum + item.price * item.quantity;
  }, 0);

  const cash = Number(input.value);

  const result = cash - total;

  receipt.innerHTML = "";

  const text = document.createElement("p");

  if (result < 0) {
    text.innerText = `Please pay additional amount: $${Math.abs(result)}`;
  } else {
    text.innerText = `Cash Returned: $${result} \nThank you!`;
  }

  receipt.appendChild(text);
});
