document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("libform");
    const storyContainer = document.getElementById("story");
  
    const stories = [
      (values) => `Once upon a time, a ${values.adjective} ${values.noun} decided to ${values.verb} with ${values.person} at ${values.place}.`,
      (values) => `${values.person} always wanted a ${values.adjective} ${values.noun} to ${values.verb} in ${values.place}.`,
      (values) => `In ${values.place}, a ${values.adjective} ${values.noun} taught ${values.person} how to ${values.verb}.`,
    ];
  
    const generateStory = (values) => {
      const randomStory = stories[Math.floor(Math.random() * stories.length)];
      return randomStory(values);
    };

    const getFormValues = () => {
      return {
        noun: document.getElementById("noun").value.trim(),
        adjective: document.getElementById("adjective").value.trim(),
        person: document.getElementById("person").value.trim(),
        verb: document.getElementById("verb").value.trim(),
        place: document.getElementById("place").value.trim(),
      };
    };

    const validateInputs = (values) => {
      return Object.values(values).every((value) => value !== "");
    };
  
    const handleFormSubmit = (event) => {
      event.preventDefault();
  
      const values = getFormValues();
      if (validateInputs(values)) {
        storyContainer.textContent = generateStory(values);
      } else {
        alert("Please fill in all fields before submitting!");
      }
    };
  
    const addShuffleButton = () => {
      const shuffleButton = document.createElement("button");
      shuffleButton.textContent = "Shuffle!";
      shuffleButton.style.marginLeft = "10px";
      shuffleButton.addEventListener("click", () => {
        const values = getFormValues();
        if (validateInputs(values)) {
          storyContainer.textContent = generateStory(values);
        } else {
          alert("Please fill in all fields before shuffling!");
        }
      });
      form.appendChild(shuffleButton);
    };

    form.addEventListener("submit", handleFormSubmit);
    addShuffleButton();
  });
  