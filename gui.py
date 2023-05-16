import functions
import PySimpleGUI as gui

label = gui.Text("Type in a Task: ")
input_box = gui.InputText(tooltip="Enter Task", key='task')
add_button = gui.Button("Add")

window = gui.Window('Task Master',
                    layout=[
                            [label, input_box, add_button]
                    ],
                    font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)

        case gui.WIN_CLOSED:
            break

window.close()

