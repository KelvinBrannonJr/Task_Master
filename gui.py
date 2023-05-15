import functions
import PySimpleGUI as gui

label = gui.Text("Type in a Task: ")
input_box = gui.InputText(tooltip="Enter Task")
add_button = gui.Button("Add")

window = gui.Window('Task Master', layout=[[label, input_box, add_button]])
window.read()
window.close()

