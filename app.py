user_task = input("Type task name: ")
clean_task = user_task.strip()

tasks = [
    "Make a sunday plan for trip",
    "Need to work on Industry standard Python projects",
    "Think about overall bad habits and make a to-do list"
]

if clean_task == "":
    print("Task cannot be empty")
else:
    tasks.append(clean_task)
    for number, task in enumerate (tasks, start= 1):
        print(number, task)
        print()
    
    done_number= int(input("Type completed task number: "))
    print("Completed Task:", tasks.pop(done_number - 1), end= "\n")

    print("Remaining tasks list\n")
    for number, task in enumerate (tasks, start= 1):
        print(number, task)