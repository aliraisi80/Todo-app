user_prompt="Enter a todo:"
todos=[]

while True:
    user_action=input("Enter add,show,edit,complete,exit:")

    if "add" in user_action:
        with open("todos.txt","r") as file:
            todos=file.readlines()
        todo=user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt","w") as file:
            file.writelines(todos)
    if "show" in user_action:
        with open("todos.txt","r") as file:
            todos=file.readlines()
        for index,todo in enumerate(todos):
            todo=todo.strip("\n")
            print(index+1,"-",todo)
    if "exit" in user_action:
        break
    if "copmlete"in user_action:
        with open("todos.txt","r") as file:
            todos=file.readlines()
        number=todo=user_action[9:]+ "\n"
        todos.pop(int(number)-1)
        with open("todos.txt","w") as file:
            file.writelines(todos)
    if "edit" in user_action:
        with open("todos.txt","r") as file:
            todos=file.readlines()
        number=todo=user_action[5:]+"\n"
        new_todo=input("Edit this todo here:")
        todos[int(number)-1]=new_todo
        with open("todos.txt","w") as file:
            file.writelines(todos)




print("Done!")