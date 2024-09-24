# # Welcome to the To-Do List App

# # Menu:
# # 1. Add a task

# if user_input == int(1):
#     print(input("What task would you like to add: "))

# # 2. View tasks

# if user_input == int(2):
#     print("Here are all of the tasks: {empty_list}")

# # 3. Mark a task as complete

# if user_input == int(3):
#     print(input("Which task would you like to mark as complete: "))

# # 4. Delete a task

# if user_input == int(4):
#     print(input("Which task would you like to delete: "))

# # 5. Quit

# if user_input.lower() == 'q':
#     print("goodbye")
#     break


tasks = []

def main():
    # I will enter my code body here

    main()


while True:
    print('Welcome to the To-Do List App!')
    print(" \n")
    print('Menu:')
    print('\n1. Add a task')
    print('\n2. View tasks')
    print('\n3. Mark a task as complete')
    print('\n4. Delete a task')
    print('\n5. Quit')
    print(" \n")
    print(" \n")

    user_input = input("Enter a number (or 'q' to quit): ").lower()

    if user_input == 'q' or user_input == '5':
        print("Goodbye!")
        break 

    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input, please enter a number or 'q' to quit.")
        continue

    # Menu:
# 1. Add a task

if user_input == 1:
    task = input("What task would you like to add: ")
    tasks.append(task)
    print(f"Task '{task}' added!")
# 2. View tasks

elif user_input == 2:
    print("Here are all of the tasks: {empty_list}")

# 3. Mark a task as complete

elif user_input == 3:
    print(input("Which task would you like to mark as complete: "))

# 4. Delete a task

elif user_input == 4:
    print(input("Which task would you like to delete: "))

# 5. Quit