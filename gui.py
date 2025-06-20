import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
#in Terminal type "pyinstaller --one file --windowed --clean gui.py" press Enter
#right click gui.py-Open in-Explorer we can see the gui file as a .exe file that can run alone
#Download HomeBrew then run the command "brew install --cask platypus" in Terminal.

sg.theme("DarkPurple4")
#search theme on google "freepysimplegui themes"
#rightclick-goto-implementation(s) to see all functions
#if using PyCharm, goto setting-plugins-tab Marketplace-rainbow brackets for better view.

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2",
                        tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_box = sg.Button("Edit")
complete_button = sg.Button(image_souce="complete.png", mouseover_color="LightBlue2",
                        tooltip="Complete", key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App', 
                    layout=[[clock],
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_box, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(value=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))
        
        case "Exit":
            break

        case 'todos':
            window[todo].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break


window(close)