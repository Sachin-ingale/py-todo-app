To-Do List App
A simple To-Do list application built with Python and Tkinter. This app allows you to add, delete, and manage tasks with a graphical user interface. Tasks are stored in a local text file (tasklist.txt) to persist across sessions.

<img width="960" alt="todo app" src="https://github.com/user-attachments/assets/7f95c786-dd1f-4c95-8b99-29a28bb91398">


Features
Add new tasks to your to-do list.
View all tasks in a scrollable list.
Delete tasks from the list.
Tasks are saved to a text file (tasklist.txt), so they persist even after closing the app.
Simple and user-friendly graphical interface.
Technologies Used
Python (3.x)
Tkinter (for building the GUI)
File I/O (to store tasks in a text file)
Installation
Prerequisites
Python 3.x should be installed on your machine.
Tkinter (comes pre-installed with Python).
Steps to Set Up
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/todo-app.git
Navigate to the project directory:

bash
Copy code
cd todo-app
Ensure you have the following image files in your project directory for the icons:

task.png (App icon)
topbar.png (Top bar image)
dock.png (Dock image)
delete.png (Delete button icon)
Run the app:

bash
Copy code
python todo_app.py
Usage
Adding a Task:

Type a task in the input field at the top and click ADD to add it to the list.
Deleting a Task:

Select a task from the list and click the Delete icon to remove it.
Persistent Tasks:

Tasks will be saved in tasklist.txt and persist even after restarting the app.
Code Structure
todo_app.py: The main Python file containing the application logic.

The app uses Tkinter for the GUI.
Task data is read from and written to tasklist.txt.
Key functions include addTask(), deleteTask(), and openTaskFile().
tasklist.txt: Stores tasks that the user adds. The app reads from this file at startup and writes back when tasks are added or removed.

Screenshots
Here you can include a screenshot of your app in action.

<!-- Replace with your screenshot -->

Contributing
If you'd like to contribute to this project:

Fork the repository.
Clone your fork:
bash
Copy code
git clone https://github.com/yourusername/todo-app.git
Make your changes, and commit them.
Push your changes and create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
Thanks to the Tkinter library for providing an easy way to build GUI applications with Python.
Inspired by various To-Do apps that help with productivity.
