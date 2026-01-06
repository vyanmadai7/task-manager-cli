Task Manager

A simple command-line task management application written in Python that allows you to create, view, complete, and delete tasks.
Features

Add tasks - Create new tasks with a title
View tasks - Display all tasks with their completion status
Mark tasks as done - Update task status when completed
Delete tasks - Remove tasks you no longer need
Persistent storage - Tasks are saved to a JSON file and persist between sessions

Requirements

Python 3.x
No external dependencies required (uses only standard library)

Installation

Download the task_manager.py file (or whatever you've named it)
Ensure you have Python 3 installed on your system
No additional setup needed!

Usage
Run the program from your terminal:
bashpython task_manager.py
```

### Menu Options

When you run the program, you'll see a menu with the following options:

1. **Show tasks** - Displays all your tasks with their status (true/false for done/not done)
2. **Add task** - Prompts you to enter a new task title
3. **Mark task done** - Select a task by number to mark it as completed
4. **Delete task** - Select a task by number to remove it permanently
5. **Exit** - Quit the application

### Example
```
Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option: 2
Enter task title: Buy groceries
Task added!
Data Storage
Tasks are automatically saved to a tasks.json file in the same directory as the script. The file is created automatically on first use and updated whenever you add, modify, or delete tasks.
JSON Structure
json[
    {
        "title": "Buy groceries",
        "done": false
    },
    {
        "title": "Finish project",
        "done": true
    }
]
Error Handling

The program handles missing tasks.json files by creating a new one
Invalid menu choices prompt you to try again
Task indexing is validated to prevent out-of-range errors

Future Improvements
Potential enhancements could include:

Task priorities or categories
Due dates
Task descriptions
Search/filter functionality
Better error messages for invalid inputs
