user_prompt="enter a todo: "
todos = []

while True:
    user_action=input("Enter add,show,edit,complete or exit: ")

    if "add" in user_action:
            with open("todos.txt","r") as file:
                todos=file.readlines()
            todo=input(user_prompt)+"\n"
            todos.append(todo)
            with open("todos.txt","w") as file:
                file.writelines(todos)
    if  "show" in user_action:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            for index,todo in enumerate(todos):
                todo = todo.strip("\n")
                print(index+1,"-",todo)
    if "exit" in user_action:
            break
    if "complete" in user_action:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number=input("Enter a number of todo to complete:")
            todos.pop(int(number)-1)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
    if "edit" in user_action:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number=input("Enter number to edit: ")
            new_todo=input("Edit this todo here: ")
            todos[int(number)-1]=new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)




print("Done!")


# filenames=["1.word.txt","2.photoshop.txt","3.excel.txt"]
#
# for filename in filenames:
#     print(filename.replace(".","-",))



# filenames=["1.word.txt","2.photoshop.txt","3.excel.txt"]
#
# for filename in filenames:
#     print(filename.replace(".","-",))
