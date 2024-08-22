import functions
import PySimpleGUI as sg
import time

clock=sg.Text(time.strftime("%b %d,%Y %H :%M:%S"),key='clock')

Label=sg.Text("tipe in a to-do")
input_box=sg.InputText(tooltip="Inter a to-do",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key="todos",
                    enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("complete")
exit_button=sg.Button("Exit")

window=sg.Window("My to-do App",
                 layout=[
                     [clock],
                     [Label],
                     [input_box,add_button],
                     [list_box,edit_button,complete_button],
                     [exit_button]
                 ],font=("Helvetice",20))

while True:
    event,values=window.read()
    # colack.Text(time.strftime("%b %d,%Y %H :%M:%S"), key='colack')


    match event:
        case"Add":
            todoS=functions.get_todos()
            new_todo=values['todo']+"\n"
            todoS.appent(new_todo)
            functions.set_todos(todoS)
            window["todos"].update(values=todoS)
        case"Eait":
            todoS=functions.get_todos()
            todo_to_edit=values['todoS'][0]
            index=todoS.index(todo_to_edit)
            todoS[index]=values['todo']
            functions.set_todos(todoS)
            window['todos'].update(values=todoS)
        case"todos":
            window['todo'].update(value=values[todoS][0])
        case"Complete":
            todoS=functions.get_todos()
            todo_to_complete=values['todos'][0]
            todoS.remove(todo_to_complete)
            functions.set_todos(todoS)
            window["todos"].update(values=todoS)
        case"Exit":
            exit()
        case WIN_CLOSED:
            break

window.close()


