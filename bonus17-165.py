import FreeSimpleGUI as sg
from converters import convert

feet = sg.Text("Enter feet:")
feet_input = sg.Input()

inch = sg.Text("Enter inches:")
inch_input = sg.Input()

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor",
                layout=[[feet,feet_input],
                        [inch, inch_input],
                        [convert_button,output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inch = float(values["inch"])

    result = convert(feet, inch)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()