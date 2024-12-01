// Array to store tasks
const tasks = [];

// Elements
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const listTasksDiv = document.querySelector(".listTasks");

// Function to add a task
function addTask(event) {
  event.preventDefault(); // Prevent form submission

  const taskText = taskInput.value.trim();
  if (taskText === "") {
    alert("Task cannot be empty!");
    return;
  }

  // Add task to array
  tasks.push(taskText);

  // Update DOM
  renderTask(taskText);

  // Clear input field
  taskInput.value = "";
}

// Function to render a single task
function renderTask(taskText) {
  // Create task container
  const taskDiv = document.createElement("div");
  taskDiv.classList.add("task");

  // Create task label with checkbox
  const labelDiv = document.createElement("div");
  labelDiv.classList.add("label");

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  const label = document.createElement("span");
  label.textContent = taskText;

  labelDiv.appendChild(checkbox);
  labelDiv.appendChild(label);

  // Create delete button
  const deleteButton = document.createElement("button");
  deleteButton.innerHTML = '<i class="fa-solid fa-xmark"></i>';

  // Add delete functionality
  deleteButton.addEventListener("click", () => {
    taskDiv.remove();
    tasks.splice(tasks.indexOf(taskText), 1); // Remove from array
  });

  // Append label and delete button to task container
  taskDiv.appendChild(labelDiv);
  taskDiv.appendChild(deleteButton);

  // Add task container to the list
  listTasksDiv.appendChild(taskDiv);
}

// Add event listener to the form
taskForm.addEventListener("submit", addTask);
