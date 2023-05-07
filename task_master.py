isLooping = True

while isLooping:
    user_choice = input("For a task, would you like to 'Add', 'Show', 'Edit', 'Complete', or 'Exit' ?:\n")
    format_choice = user_choice.title().strip()

    match format_choice:
        case 'Add':
            task = input("Enter a Task: ") + "\n"
            format_task = task.title()

            # With context manager - same as file.open() but, it automatically closes file after context scope
            with open("tasks.txt", 'r') as file:
                tasks = file.readlines()

            tasks.append(format_task)

            with open("tasks.txt", 'w') as file:
                file.writelines(tasks)

        case 'Show':
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

        case 'Edit':
            edit_number = int(input("Starting with 1, which item number in the collection do you want to edit? "))
            edit_number = edit_number - 1

            with open("tasks.txt", 'r') as file:
                tasks = file.readlines()

            new_task = input("What would you like to change this to? ")
            tasks[edit_number] = new_task.title() + '\n'

            with open("tasks.txt", 'w') as file:
                file.writelines(tasks)

        case 'Complete':
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

        case 'Exit':
            isLooping = False
            break

        case no_match:
            print("Sorry that is not a valid choice...")

print("Exiting program, goodbye..")
