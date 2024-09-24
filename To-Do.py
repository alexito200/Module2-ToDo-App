# # Welcome to the To-Do List App

tasks = []

while True:
    print('\nWelcome to the To-Do List App!')
    print('\nMenu:')
    print('\n1. Add a task')
    print('\n2. View tasks')
    print('\n3. Mark a task as complete')
    print('\n4. Delete a task')
    print('\n5. Quit')
    print(" \n")

    user_input = input("Enter a number (or 'q' to quit): ").lower()

    if user_input == 'q':
        print("Goodbye!")
        break 

    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input, please enter a number or 'q' to quit.")
        # continue
    
    if user_input == 5:
        print("Goodbye!")
        break

# Menu:
# 1. Add a task
    if user_input == 1:
        while True:
            task = input("\nWhat task would you like to add? (or type 'back' to return to main menu): ").lower()
            if task == 'back':
                break
            tasks.append(f"{task} (Incomplete)")
            print(f"\nTask '{task} (Incomplete)' added! Here is the updated list of tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"\n{i}. {t}")
# 2. View tasks
    elif user_input == 2:
        while True:
            if tasks:
                print("\nHere are all of the tasks: ")
                for i, task in enumerate (tasks, 1):
                    print(f"\n{i}. {task}")
            else:
                print("Your task list is empty")
            back_option = input("\nType 'back' to return to main menu: ").lower()
            if back_option == 'back':
                break

# 3. Mark a task as complete
    elif user_input == 3:
        while True:
            if tasks:
                print("\n Here are your new tasks:")
                for i, task in enumerate (tasks, 1):
                    print(f"\n{i}. {task}")
                try:
                    task_num = input("\nEnter the number of the task to mark as complete (or type 'back' to return): ")
                    if task_num.lower() == 'back':
                        break
                    task_num = int(task_num)
                    if 1 <= task_num <= len(tasks):
                        completed_task = tasks[task_num - 1]
                        tasks[task_num - 1] = completed_task.replace(" (Incomplete)", " (Complete)")
                        print(f"\nTask '{completed_task}' marked as complete!")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to mark as complete.\n")
                break

# 4. Delete a task
    elif user_input == 4:
        while True:
            if tasks:
                print("\nHere are your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"\n{i}. {task}")
                try:
                    task_num = input("\nEnter the number of the task you want to delete (or type 'back' to return): ")
                    if task_num.lower() == 'back':
                        break
                    task_num = int(task_num)
                    if 1 <= task_num <= len(tasks):
                        deleted_task = tasks.pop(task_num - 1)
                        print(f"\nTask '{deleted_task}' has been deleted!")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to delete.\n")
                break