Task Manager CLI
A command-line task manager built with Python. Track your to do items with persistent storage and a simple, intuitive interface.
Overview
This is a straightforward task management application that runs in your terminal. It stores tasks in a JSON file, making them persistent across sessions. The application is designed to be simple, fast, and require zero external dependencies.
Features

View all tasks with their completion status
Add new tasks with custom titles
Mark tasks as complete
Delete tasks you no longer need
Automatic saving to disk after every operation
Built entirely with Python's standard library

Requirements

Python 3.x
No external packages required

Installation
Download or clone the repository to your local machine:
bashgit clone <https://github.com/vyanmadai7/task-manager-cli.git>
cd task-manager
Run the application:
bashpython task_manager.py
```

The application will create a `tasks.json` file in the same directory on first use.

## Usage

When you run the program, you'll see an interactive menu:
```
Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option:
Available Commands
1. Show tasks - Displays all your tasks numbered with their status (true for completed, false for pending)
2. Add task - Prompts you to enter a task title and adds it to your list
3. Mark task done - Shows your task list and lets you select which task to mark as complete
4. Delete task - Shows your task list and lets you select which task to remove
5. Exit - Closes the application
Example Session
bash$ python task_manager.py

Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option: 2
Enter task title: Review project documentation
Task added!

Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option: 1
1. Review project documentation [false]

Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option: 3
1. Review project documentation [false]
Enter task number to mark done: 1
Task marked done!
Data Storage
Tasks are stored in tasks.json in the application directory. The file structure is simple:
json[
    {
        "title": "Review project documentation",
        "done": true
    },
    {
        "title": "Update README file",
        "done": false
    }
]
You can manually edit this file if needed, though the application handles all standard operations.
Code Structure
The application is organized into these main functions:

load_tasks() - Reads tasks from the JSON file, returns empty list if file doesn't exist
save_tasks(tasks) - Writes the current task list to the JSON file
show_tasks(tasks) - Prints all tasks with their index and completion status
add_task(tasks) - Handles user input for creating new tasks
mark_done(tasks) - Updates a task's status to completed
delete_task(tasks) - Removes a task from the list
main() - Main program loop that displays the menu and handles user choices

Error Handling
The application includes basic error handling:

Creates a new tasks file if one doesn't exist
Validates task indices to prevent out-of-range errors
Handles invalid menu selections by prompting to try again
Displays appropriate messages when the task list is empty

Limitations

No input validation for non-numeric entries when selecting tasks
No confirmation prompt before deleting tasks
Tasks are limited to single-line titles
No support for task descriptions, priorities, or due dates
No ability to edit existing task titles

Possible Improvements
This is a minimal viable product that could be enhanced with:

Task priorities or importance levels
Due dates and time tracking
Task categories or tags
Multi-line descriptions for tasks
Search and filter functionality
Ability to edit task titles
Confirmation prompts for destructive operations
Better input validation and error messages
Export to other formats like CSV or Markdown
Statistics on task completion

Contributing
This is an educational project intended to demonstrate basic Python concepts including file I/O, JSON handling, and CLI application structure. Feel free to fork and modify for your own use.
