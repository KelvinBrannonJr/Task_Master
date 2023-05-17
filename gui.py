import functions
import PySimpleGUI as gui
import time

# Design Theme
gui.theme("DarkBlue14")

# Date and Time element
clock = gui.Text("", key='clock')

# ADD GUI elements
label_add = gui.Text("Type in a Task: ")
input_box_add = gui.InputText(tooltip="Enter Task", key='task')
add_button = gui.Button("Add")

# Edit GUI elements
label_edit = gui.Text("Your Tasks:")
list_box = gui.Listbox(values=functions.get_tasks(), key='tasks', enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")

# Complete GUI element
complete_button = gui.Button("Complete")

# Exit GUI element
exit_button = gui.Button("Exit")


# GUI window layout
window = gui.Window('Task Master',
                    layout=[
                            [clock],
                            [label_add, input_box_add, add_button],
                            [label_edit],
                            [list_box, edit_button, complete_button],
                            [exit_button]
                    ],
                    font=('Helvetica', 15))

# Connecting GUI elements with backend Functionality
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")

        case "Edit":
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task']

                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value="")

            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 20))

        case "Complete":
            try:
                task_to_complete = values['tasks'][0]
                tasks = functions.get_tasks()
                tasks.remove(task_to_complete)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value="")
            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break

        case "tasks":
            window['task'].update(value=values['tasks'][0])

        case gui.WIN_CLOSED:
            break


window.close()

