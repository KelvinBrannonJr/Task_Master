import functions
import time


# Time format
current_time = time.strftime("%b %d %Y %H:%M:%S")
print("Currently it is", current_time)

# Event loop for user input
while True:
    user_choice = input("For a task, would you like to 'Add', 'Show', 'Edit', 'Complete', or 'Exit'?: ").title()
    format_choice = user_choice.strip()

    # Add - to add a task to list
    if 'Add' in user_choice:
        task = input("Enter a Task: ").title()
        format_task = task.strip()

        tasks = functions.get_tasks()

        tasks.append(format_task + "\n")

        functions.write_tasks(tasks)

    # Show - to show tasks in the current list
    elif 'Show' in user_choice:
        tasks = functions.get_tasks()

        # List Comprehension to task items and return it in a new collection
        new_tasks = [item.strip('\n') for item in tasks]

        for index, item in enumerate(new_tasks):
            row = f"{index + 1} - {item}"
            print(row)

    # Edit - get a task in the list at it's index and overwrite the value
    elif 'Edit' in user_choice:
        # try catch exception block
        try:
            edit_number = int(input("Starting with 1, which item number in the collection do you want to edit? "))
            edit_number = edit_number - 1

            tasks = functions.get_tasks()

            new_task = input("What would you like to change this to? ")
            tasks[edit_number] = new_task.title() + '\n'

            functions.write_tasks(tasks)

        # continue will rerun the while loop back at the top, nothing below will execute
        except ValueError:
            print("Invalid selection of item..Use only the number next to task item")
            continue

    # Complete and remove task from the list
    elif 'Complete' in user_choice:
        try:
            complete = int(input("Enter a number of task you have completed: \n"))

            tasks = functions.get_tasks()

            selected_index = complete - 1
            completed_task = tasks[selected_index].strip('\n')
            tasks.pop(selected_index)

            functions.write_tasks(tasks)

            message = f"Task: {completed_task}, was completed and removed"
            print(message)
        except IndexError:
            print("That item number does not exist..")
            continue

    # User enters Exit to terminate the program
    elif 'Exit' in user_choice:
        break

    # Else to handle invalid entry
    else:
        print("Sorry that is not a valid choice...")

print("Exiting program, goodbye..")


