document.addEventListener("DOMContentLoaded", () => {
    const gridContainer = document.querySelector("#grid-container");
    const DEFAULT_GRID_SIZE = 16;
    const DEFAULT_CONTAINER_SIZE = 500;
    const colorPicker = document.querySelector("#color-picker");
    const resetButton = document.querySelector("#reset-button");
    const clearAllButton = document.querySelector("#clear-all-button");
    const gridSizeInput = document.querySelector("#grid-size");
    const gridWidthInput = document.querySelector("#grid-width");
    const gridHeightInput = document.querySelector("#grid-height");
    const gridGapInput = document.querySelector("#grid-gap");
    const eraserButton = document.querySelector("#eraser-button");
    let selectedColor = "#000000"; // Default color
    let gridSize = 16; // Default grid size
    let isMouseDown = false; // Track mouse state
    let isEraserMode = false; // Track eraser mode state
  
    // Set the color picker
    colorPicker.addEventListener("input", (e) => {
      selectedColor = e.target.value;
      isEraserMode = false; // Disable eraser mode when a new color is picked
      eraserButton.classList.remove("active"); // Visually deselect the eraser
    });
  
    // Toggle eraser mode
    eraserButton.addEventListener("click", () => {
      isEraserMode = !isEraserMode;
      eraserButton.classList.toggle("active"); // Highlight the button if active
    });
  
    // Create the grid
    function createGrid(size) {
      gridContainer.innerHTML = ""; // Clear the grid
      gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
      gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;
  
      for (let i = 0; i < size * size; i++) {
        const square = document.createElement("div");
        square.classList.add("square");
        square.style.backgroundColor = "#ffffff"; // Default color
        gridContainer.appendChild(square);
      }
    };
  
    // Add event listeners for "press-and-hold" functionality
    gridContainer.addEventListener("mousedown", () => {
      isMouseDown = true;
    });
  
    gridContainer.addEventListener("mouseup", () => {
      isMouseDown = false;
    });
  
    gridContainer.addEventListener("mouseleave", () => {
      isMouseDown = false; // Ensure coloring stops if the mouse leaves the grid
    });
  
    gridContainer.addEventListener("mouseover", (e) => {
      if (isMouseDown && e.target.classList.contains("square")) {
        e.target.style.backgroundColor = isEraserMode ? "#ffffff" : selectedColor; // Erase or color
      }
    });
  
    gridContainer.addEventListener("click", (e) => {
      if (e.target.classList.contains("square")) {
        e.target.style.backgroundColor = isEraserMode ? "#ffffff" : selectedColor; // Single-click erase or color
      }
    });
  
    // Reset button functionality
    resetButton.addEventListener("click", resetGrid);
    
    // Function to reset the grid to default
    function resetGrid() {
    // Reset the grid container to default size (500px x 500px)
    gridContainer.style.width = `${DEFAULT_CONTAINER_SIZE}px`;
    gridContainer.style.height = `${DEFAULT_CONTAINER_SIZE}px`;
  
    // Regenerate the grid with default size of 16x16
    gridSize = DEFAULT_GRID_SIZE; // Reset grid size to default
    createGrid(gridSize);
  
    // Clear any active modes (hover, eraser, etc.)
    isMouseDown = false;
    isEraserMode = false;
    eraserButton.classList.remove("active");

    // Reset the grid size input field, if applicable
    if (gridSizeInput) {
    gridSizeInput.value = DEFAULT_GRID_SIZE;
      }
    };
  
    // Regenerate grid with a given size (16x16 default)
    function generateGrid(size) {
    gridContainer.innerHTML = '';  // Clear the container
    gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
    gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;
    // Create grid items
    for (let i = 0; i < size * size; i++) {
      const gridItem = document.createElement('div');
      gridItem.classList.add('grid-item');
      gridContainer.appendChild(gridItem);
  
      // Add event listeners for coloring
      gridItem.addEventListener('mousedown', colorGridItem);
      gridItem.addEventListener('mouseover', colorGridItem);
        }
    };
    // Clear all functionality
    clearAllButton.addEventListener("click", () => {
      const squares = document.querySelectorAll(".square");
      squares.forEach((square) => {
        square.style.backgroundColor = "#ffffff"; // Clear all squares
      });
    });
  
    // Update grid container properties dynamically
    function updateGridContainer() {
      gridContainer.style.width = `${gridWidthInput.value}px`;
      gridContainer.style.height = `${gridHeightInput.value}px`;
      gridContainer.style.gap = `${gridGapInput.value}px`;
      createGrid(gridSize); // Recreate grid to fit new container size
    };
  
    // Attach event listeners to input fields for dynamic resizing
    [gridWidthInput, gridHeightInput, gridGapInput].forEach((input) => {
      input.addEventListener("change", updateGridContainer);
    });
  
    // Update grid size on input change
    gridSizeInput.addEventListener("change", (e) => {
      gridSize = parseInt(e.target.value, 10);
      createGrid(gridSize);
    });
  
    // Initialize the grid
    createGrid(gridSize);
  });
  