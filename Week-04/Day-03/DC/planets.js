// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?

const planets = [
    {name: "Mercury", color: "gray", moons: [] },
    {name: "Venus", color: "yellow", moons: [] },
    {name: "Earth", color: "blue", moons: 1 },
    {name: "Mars", color: "red", moons: 2 },
    {name: "Jupiter", color: "orange", moons: 4 },
    {name: "Saturn", color: "gold", moons: 4 },
    {name: "Uranus", color: "lightblue", moons: 5 },
    {name: "Neptune", color: "darkblue", moons: 2 },
];

const section = document.querySelector(".listPlanets");

// Loop through the planets array
planets.forEach((planet) => {
  // Create a div for the planet
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planet.color; // Assign planet's background color
  planetDiv.textContent = planet.name; // Add planet's name

  // Create and append moons
for (let i = 0; i < planet.moons;i++) {
  const moonDiv = document.createElement("div")
  moonDiv.classList.add("moon")
  moonDiv.style.left = i*10+"px"
  planetDiv.appendChild(moonDiv)
}


  section.appendChild(planetDiv); // Append the planet to the section
});