import functions
import PySimpleGUI as gui

# ADD GUI elements
label = gui.Text("Type in a Task: ")
input_box = gui.InputText(tooltip="Enter Task", key='task')
add_button = gui.Button("Add")

# Edit GUI elements
label_tasks = gui.Text("Your Tasks:")
list_box = gui.Listbox(values=functions.get_tasks(), key='tasks', enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")

# Complete GUI elements
complete_button = gui.Button("Complete")

# Exit GUI elements
exit_button = gui.Button("Exit")


# GUI window layout
window = gui.Window('Task Master',
                    layout=[
                            [label, input_box, add_button],
                            [label_tasks],
                            [list_box, edit_button, complete_button],
                            [exit_button]
                    ],
                    font=('Helvetica', 15))

# Connecting GUI elements with backend Functionality
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['tasks'])
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Complete":
            task_to_complete = values['tasks'][0]
            tasks = functions.get_tasks()
            tasks.remove(task_to_complete)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")

        case "Exit":
            break

        case "tasks":
            window['task'].update(value=values['tasks'][0])

        case gui.WIN_CLOSED:
            break


window.close()

