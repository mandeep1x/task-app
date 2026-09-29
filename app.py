user_task = input("Type your favourite task: ")
clean_task = user_task.strip()

tasks = [
    "I have a Laptop",
    "I also have a Mobile phone",
    "I also have a workspace for coding in my home"
]

if clean_task == "":
    print("Task cannot be empty")
else:
    tasks.append(clean_task)
    for each_item in tasks:
        print(each_item)
