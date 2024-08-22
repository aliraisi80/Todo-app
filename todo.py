# import functions
from functions import get_todos,set_todos

user_prompt="enter a todo:"
todos = []

while True:
    user_action=input("Enter add,show,edit,complete or exit: ")

    if user_action.startswith("add"):
            todos=get_todos()
            todo=user_action[4:]+"\n"
            todos.append(todo)
            set_todos(todos)
    if user_action.startswith("show"):
            todos =get_todos()
            for index,todo in enumerate(todos):
                todo = todo.strip("\n")
                print(index+1,"-",todo)
    if user_action.startswith("exit"):
            break
    if user_action.startswith("complete"):
        try:
                todos =get_todos()
                number=todo=user_action[9:]+"\n"
                todos.pop(int(number)-1)
                set_todos(todos)
        except IndexError:
            print("your Index is out of range")
    if user_action.startswith("edit"):
        try:
                todos =get_todos()
                number=todo=user_action[5:]
                new_todo=input("Edit this todo here: ")+"\n"
                todos[int(number)-1]=new_todo
                set_todos(todos)
        except IndexError:
            print("your Index is out of range")




print("Done!")