isLooping = True

while isLooping:
    user_choice = input("For a task, would you like to 'Add', 'Show', 'Edit', 'Complete', or 'Exit' ?:\n").title()
    format_choice = user_choice.strip()

    if 'Add' in user_choice:
        task = input("Enter a Task: ").title()
        format_task = task.strip() + "\n"

        # With context manager - same as file.open() but, it automatically closes file after context scope
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()

        tasks.append(format_task)

        with open("tasks.txt", 'w') as file:
            file.writelines(tasks)

    elif 'Show' in user_choice:
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()

        # List Comprehension - inline for-loop returns a list without declaring empty list for new items.
        new_tasks = [item.strip('\n') for item in tasks]

        # Same way but with a for-loop ** Longer route but same as list comprehension
        # new_tasks = []
        # for item in tasks:
        #     item = item.strip('\n')
        #     new_tasks.append(item)
        #
        for index, item in enumerate(new_tasks):
            row = f"{index + 1} - {item}"
            print(row)

    elif 'Edit' in user_choice:
        edit_number = int(input("Starting with 1, which item number in the collection do you want to edit? "))
        edit_number = edit_number - 1

        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()

        new_task = input("What would you like to change this to? ")
        tasks[edit_number] = new_task.title() + '\n'

        with open("tasks.txt", 'w') as file:
            file.writelines(tasks)

    elif 'Complete' in user_choice:
        complete = int(input("Enter a number of task you have completed: \n"))

        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()

        selected_index = complete - 1
        completed_task = tasks[selected_index].strip('\n')
        tasks.pop(selected_index)

        with open("tasks.txt", 'w') as file:
            file.writelines(tasks)

        message = f"Task: {completed_task}, was completed and removed"
        print(message)

    elif 'Exit' in user_choice:
        isLooping = False
        break

    else:
        print("Sorry that is not a valid choice...")

print("Exiting program, goodbye..")
