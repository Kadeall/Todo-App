import FreeSimpleGUI as ki

label =ki.Text("Enter feet")
input = ki.Input()
label1 =ki.Text("Enter inches")
input1 = ki.Input()

add_button = ki.Button("Converter")

window = ki.Window('Converter', layout = [[label, input],[label1, input1],[add_button]])

window.read()
window.close()