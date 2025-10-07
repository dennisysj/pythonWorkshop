#Step 1: Create a list to hold your tasks
tasks = []

#Step 2: Create a main menu (should it have a loop?)
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")
    #Step 3: Add If blocks to process the choice the user made

    #Step 4: Add task
    #Step 5: Remove task
    #Step 6: View Tasks
    #Step 7: Quit


    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f'"{task}" added.')

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        num = int(input("Enter the number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f'"{removed}" removed.')
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
