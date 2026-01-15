# Task Manager CLI

A very simple command-line task manager written in Python. It lets you add, view, complete, and delete tasks directly from the terminal. Tasks are saved in a JSON file so they stay even after you close the program.

---

Overview

This is a simple terminal-based task manager. It stores all tasks in a single JSON file (tasks.json). The main goal of this project is to keep the code clean, easy to understand, and built only with Python’s standard library.

---

## Features

* Show all tasks with their completion status (`true` or `false`)
* Add new tasks with a title
* Mark existing tasks as done
* Delete tasks from the list
* Tasks are automatically saved after every change
* Uses only Python’s standard library (no external packages)

---

## Requirements

* Python 3.x
* No third-party libraries

---

## Installation

Clone the repository:

```bash
git clone https://github.com/vyanmadai7/task-manager-cli.git
cd task-manager-cli
```

Run the program:

```bash
python task_manager.py
```

The program will create a `tasks.json` file automatically if it does not exist.

---

## Usage

When you run the program, you will see this menu:

```
Task Manager
1. Show tasks
2. Add task
3. Mark task done
4. Delete task
5. Exit
Choose an option:
```

### Menu Options

1. **Show tasks** – Displays all tasks with their index number and status
2. **Add task** – Prompts for a task title and adds it to the list
3. **Mark task done** – Marks a selected task as completed
4. **Delete task** – Removes a selected task
5. **Exit** – Closes the application

---

## Example

```bash
Choose an option: 2
Enter task title: Review project documentation
Task added!

Choose an option: 1
1. Review project documentation [false]

Choose an option: 3
Enter task number to mark done: 1
Task marked done!
```

---

## Data Storage

Tasks are stored in `tasks.json` in the project directory. Each task has a title and a completion flag:

```json
[
  {
    "title": "Review project documentation",
    "done": true
  }
]
```

---

## Code Structure

The program is divided into small, readable functions:

* `load_tasks()` – Loads tasks from `tasks.json` if it exists
* `save_tasks(tasks)` – Saves tasks to the JSON file
* `show_tasks(tasks)` – Prints all tasks and their status
* `add_task(tasks)` – Adds a new task
* `mark_done(tasks)` – Marks a task as completed
* `delete_task(tasks)` – Deletes a task
* `main()` – Runs the menu loop and handles user choices

---

## Error Handling

* Creates an empty task list if `tasks.json` does not exist
* Prevents crashes when task numbers are out of range
* Handles invalid menu choices by asking again

---

## Limitations

* No validation for non-numeric input when entering task numbers
* No confirmation before deleting a task
* Task titles are single-line only
* Tasks cannot be edited after creation
* No priorities, due dates, or descriptions

---

## Possible Improvements

* Add input validation
* Allow editing task titles
* Add task priorities or due dates
* Add confirmation before deleting tasks
* Add search or filter options
* Improve task status display (done / pending instead of true / false)

---
