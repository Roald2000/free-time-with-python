# TODO LIST APP


import pprint 


class MyToDoApp:
    
    def __init__(self) -> None:
        self.todo_list = []
        
    def view_todo(self)-> None:
        print()
        pprint.pprint(self.todo_list)
        print()
        
    def add_todo(self,todo) -> None:
        self.todo_list.append(todo)
        self.view_todo()        
    
    def update_todo(self,old_todo,new_todo) -> None:
        if old_todo not in self.todo_list:
            raise Exception("Invalid Todo Not Found")
        else:            
            old_todo_index = self.todo_list.index(old_todo)
            self.todo_list[old_todo_index] = new_todo        
            self.view_todo()
                                    
    def delete_todo(self,todo)-> None:
        for item in self.todo_list:
            if item == todo:
                self.todo_list.remove(todo)
            else:
                raise Exception("Invalid Todo Not Found")
        self.view_todo()
        

def prompt_input(prompt,noSpace = True):
    try:
        myInput = input(prompt).replace(" " if noSpace else "" ,"")
        if myInput is None:
            raise ValueError("Must Have an Input")
        else:
            return myInput
    except ValueError:
        print("Error")
        
todo = MyToDoApp()

while True: 
    try:
        choices = ['a','b','c','d','e']
        print("a. View Todo\nb. Add Todo\nc. Update Todo\nd. Delete Todo\ne.Exit")
        user_choice = prompt_input("Enter Choice: ",True).lower()
        if user_choice not in choices:
            raise Exception("Invalid Choice")
        else:
            if user_choice == 'a':
                todo.view_todo()
            elif user_choice == 'b':
                user_todo = prompt_input("Add To do: ",noSpace=False)
                todo.add_todo(user_todo)
            elif user_choice == 'c':
                old_user_todo = prompt_input("Enter To do: ",noSpace=False)
                new_user_todo = prompt_input(f"Replace '{old_user_todo}' To do: ", noSpace=False)
                todo.update_todo(old_user_todo,new_user_todo)
            elif user_choice == 'd':
                delete_todo = prompt_input("Enter To do: ",noSpace=False)
                todo.delete_todo(delete_todo)
            elif user_choice == 'e':
                break
    except Exception as ExError:
        print()
        pprint.pprint("ERROR: ",ExError)
        print()
    