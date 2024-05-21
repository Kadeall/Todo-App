import function
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter a todo")

add_button = sg.Button("Add")

window = sg.Window('MY To-Do App', layout=[[label],[input_box, add_button]])
window.read()
window.close()