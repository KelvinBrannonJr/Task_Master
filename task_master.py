isLooping = True

while isLooping:
    user_choice = input("For a task, would you like to 'Add', 'Show', 'Edit', 'Complete', or 'Exit' ?:\n")
    format_choice = user_choice.title().strip()

    match format_choice:
        case 'Add':
            task = input("Enter a Task: ") + "\n"
            format_task = task.title()

            file = open("tasks.txt", 'r')
            tasks = file.readlines()
            file.close()

            tasks.append(format_task)

            file = open('tasks.txt', 'w')
            file.writelines(tasks)
            file.close()

            print(format_task)

        case 'Show':
            file = open("tasks.txt", 'r')
            tasks = file.readlines()
            file.close()

            for index, format_task in enumerate(tasks):
                row = f"{index + 1} - {format_task}"
                print(row)

        case 'Edit':
            print(task_array)
            edit_choice = int(input("Starting with 1, which item number in the collection do you want to edit? "))
            refactored_index = edit_choice - 1

            new_task = input("What would you like to change the task to? ")
            print(new_task)

            task_array[refactored_index] = new_task.title().strip()
            print("Ok your changes have been made.", task_array)

        case 'Complete':
            complete = int(input("Enter a number of task you have completed: \n"))
            task_array.pop(complete - 1)

        case 'Exit':
            isLooping = False
            break

        case no_match:
            print("Sorry that is not a valid choice...")

print("Exiting program, goodbye..")



