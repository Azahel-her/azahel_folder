# A simple to-do list manager for high school students using functions and list

# Initial to-do list
# Function to display the current to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice",
"piano"]
def display_todo_list():
    print(f"to do:\n")
    for elements in todo_list:
        print(elements)
   
   
def add_newtask():
        new_task=input("insert a new task:")
        todo_list.append(new_task)
        display_todo_list()
        

def remove_task():
    delete_task = input("what task you want to remove?:")
    if delete_task in todo_list:
        todo_list.remove(delete_task)
        display_todo_list()
    else:
        print("not valid task")
       
     
       

# Function to find the index of a task
def find_task():
    position= input("what task you want to know?:")
    if position in todo_list:
        print("your task is number:")
        print(todo_list.index(position))
        
        
#The user wants to know in what position is a task.
# Function to complete and remove the first task
def complete_task():
    remove_first_task= input("do you wanna remove the first one?:")
    if remove_first_task == "yes":
        print("you delete the first task")
        del todo_list[0]
        display_todo_list()
    elif remove_first_task == "no":
        print("no problem")
        display_todo_list()
    else :
        print("not valid")
    
#The user wants to remove the first task.

# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks():
    keyword = input("what you want to look for?:")
    item =[item for item in todo_list if keyword in item]
    print(item)
 


    
    
#TODO create a list comprehension variable to filter tasks containing a
#specific keyword
#filtered_tasks = []
#print(f"\nTasks containing '{keyword}':")
#print(filtered_tasks if filtered_tasks else "No tasks found.")
# Main program
# Main menu to choose options
def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        choice = input("enter your number:")
        if choice == "1":
            display_todo_list()
        elif choice == "2":
            add_newtask()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            find_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            filter_tasks()
            

main()

