"""

TODO: REFACTOR TO OBJECT-ORIENTED PROGRAMMING (OOP)
Next Steps for Implementation:
1. Create a `TaskManager` or `TodoList` class.
2. Initialize the class with the task list (`self.tasks`) and `file_name`.
3. Move all the standalone functions inside the class as methods.
4. Convert procedural data updates to use class attributes (`self`).

"""

import json
import os
from dotenv import load_dotenv

load_dotenv()
file_name = os.getenv("FILE_NAME")

if not file_name:
    file_name = "tasks.json"


def load_tasks():
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_tasks(task_list):
    with open(file_name, "w") as file:
        json.dump(task_list, file, indent=4)


def show_task(task_list):
    if not task_list:
        print("Task list is empty")
        return

    print("\n-----Current tasks-----")
    for number, task in enumerate(task_list, start=1):
        print(f"{number}. {task}")
    print(f"Total Tasks - {len(task_list)}")


def add_task(task_list):
    user_task = input("\nType new task name: ")
    clean_task = user_task.strip()

    if clean_task == "":
        print("Task cannot be empty")
    else:
        task_list.append(clean_task)
        save_tasks(task_list)
        print(f"Success: {clean_task} added")


def complete_task(task_list):
    if not task_list:
        print("No one task is completed")
        return

    try:

        complete = int(input("\nType completed task number: "))
        if complete > len(task_list) or complete < 1:
            print("Try again This number does not exist")
        else:
            print("Completed Task:", task_list.pop(complete - 1))
            save_tasks(task_list)

    except ValueError:
        print("Please fill the right number")


tasks = load_tasks()

if not tasks:
    tasks = ["Make a sunday plan for trip",
             "Need to work on Industry standard Python projects",
             "Think about overall bad habits and make a to-do list"]

    save_tasks(tasks)

while True:
    print("\n---------You have four choices---------")
    print("1. Show List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit Choice")

    try:
        user_choice = int(input("Choose one option in (1-4): "))
        if not user_choice:
            print("Please type something before proceed")
        elif user_choice > 4 or user_choice < 1:
            print("Please type the Correct value in 1 to 4")
        elif user_choice == 1:
            show_task(tasks)
        elif user_choice == 2:
            add_task(tasks)
        elif user_choice == 3:
            complete_task(tasks)
        elif user_choice == 4:
            print("Exit the Options")
            break

    except ValueError:
        print("Type the Right Value (numbers only)\n")
