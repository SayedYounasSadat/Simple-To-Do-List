tasks = []

while True:
    print("Simple To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter Your Choice (1-3)")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(f'task "{task}" added.')

    elif choice == "2":
        if tasks:
            print("\nYour To-Do List:")
            for task in tasks:
                print(f"- {task}")
        else:
            print("There are no tasks to show")
    
    elif choice == "3":
        print("Exiting the application\nDone")
        break

    else:
        print("Invalid choise: please enter a number from 1 -3")