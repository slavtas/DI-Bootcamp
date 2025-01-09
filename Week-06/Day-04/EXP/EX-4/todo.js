export class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    addTask(task) {
      this.tasks.push({ task, completed: false });
    }
  
    completeTask(index) {
      if (this.tasks[index]) {
        this.tasks[index].completed = true;
      }
    }
  
    listTasks() {
      return this.tasks
        .map((taskObj, index) => {
          return `${index + 1}. ${taskObj.task} [${
            taskObj.completed ? "✔️" : "❌"
          }]`;-3
          
        })
        .join("\n");
    }
  }