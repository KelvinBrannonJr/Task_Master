# from functions import get_tasks, write_tasks # *** Same as below but have to write functions out one by one.
import functions
import time

isLooping = True

current_time = time.strftime("%b %d %Y %H:%M:%S")
print("Currently it is", current_time)

while isLooping:
    user_choice = input("For a task, would you like to 'Add', 'Show', 'Edit', 'Complete', or 'Exit'?: ").title()
    format_choice = user_choice.strip()

    if 'Add' in user_choice:
        task = input("Enter a Task: ").title()
        format_task = task.strip()

        tasks = functions.get_tasks()

        tasks.append(format_task + "\n")

        functions.write_tasks(tasks)

    elif 'Show' in user_choice:
        tasks = functions.get_tasks()

        # List Comprehension - inline for-loop returns a list without declaring empty list for new items.
        new_tasks = [item.strip('\n') for item in tasks]

        # Same way but with a for-loop ** Longer route but same as list comprehension
        # new_tasks = []
        # for item in tasks:
        #     item = item.strip('\n')
        #     new_tasks.append(item)

        for index, item in enumerate(new_tasks):
            row = f"{index + 1} - {item}"
            print(row)

    elif 'Edit' in user_choice:
        try:
            edit_number = int(input("Starting with 1, which item number in the collection do you want to edit? "))
            edit_number = edit_number - 1

            tasks = functions.get_tasks()

            new_task = input("What would you like to change this to? ")
            tasks[edit_number] = new_task.title() + '\n'

            functions.write_tasks(tasks)

        except ValueError:
            print("Invalid selection of item..Use only the number next to task item")
            continue  # continue - will rerun the while loop back at the top, nothing below will execute

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

    elif 'Exit' in user_choice:
        isLooping = False
        break

    else:
        print("Sorry that is not a valid choice...")

print("Exiting program, goodbye..")


