def show_task(task_list):
    if not task_list:
        print("Task list is empty")
        return

    print("\n-----Current tasks-----")
    for number, task in enumerate (task_list, start= 1):
        print(f"{number}. {task}")
    print(f"Total Tasks - {len(task_list)}")


def add_task(task_list):
    user_task = input("\nType new task name: ")
    clean_task = user_task.strip()

    if clean_task == "":
        print("Task cannot be empty")
    else:
        task_list.append(clean_task)
        print(f"Success: {clean_task} added")

        
def complete_task(task_list):
    if not task_list:
        print("No one task is completed")
        return
    
    try:

        complete= int(input("\nType completed task number: "))
        if complete > len(task_list) or complete < 1:
            print("Try again This number does not exist")
        else:
            print("Completed Task:", task_list.pop(complete - 1))
    
    except ValueError:
        print("Please fill the right number")


tasks = ["Make a sunday plan for trip",
    "Need to work on Industry standard Python projects",
    "Think about overall bad habits and make a to-do list"]


while True:
    print("\n---------You have four choices---------")
    print("1. Show List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit Choice")


