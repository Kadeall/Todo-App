import function
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")

add_button = sg.Button("Add")

window = sg.Window('MY To-Do App', layout=[[label],[input_box, add_button]],
                   font=('Helvetica',20))



while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.opening_files()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)



window.close()