todo_list = []

def show_menu():
    print("\nTodo List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter the number (1-4): ")

    if choice == "1":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print("{}. {}".format(i, task))

    elif choice == "2":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully.")

    elif choice == "3":
        if not todo_list:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter the task number: "))
            if 1 <= task_no <= len(todo_list):
                removed = todo_list.pop(task_no - 1)
                print("{} removed successfully.".format(removed))
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Good Bye!")
        break

    else:
        print("Invalid input. Please try again!")

print("Thank you!")