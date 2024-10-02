# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
students = [
    "Liam Chen",
    "Ava Patel",
    "Noah Ramirez",
    "Emma Johnson",
    "Ethan Kim",
    "Sophia Nguyen",
    "Mason Brown",
    "Isabella Martinez",
    "Aiden Lee",
    "Mia White"
]


def display_students():
    print(f"Current students:\n")
    #TODO HINT: Print each student in the 'students' list
    for elements in students:
        print(elements)
  
    

# Add a new student to the list
def add_student():
    #TODO HINT: Ask the user for the student's name.
    new_name = input("insert a name:")
    #TODO Append the student's name to the 'students' list
    #TODO display the updated list
    students.append(new_name)
    for elements in students:
       print(elements)

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to remove
    delete_name = input("what name you want to delete?:")
    #TODO Check if the student is in the list, then remove it
    #TODO If the student is not found, print an error message
    #TODO display the updated list
    if delete_name in students:
        students.remove(delete_name)
        for i in students:
            print(i)
            
    else:
        print("not valid name")

# remove a student from the end of the list
def pop_student():
    #TODO HINT: Remove the last student from the list
   if len(students) == 0:
       print("that list is empty")
   else:
       print("the name you deleted is:")
       print(students[-1])
       students.pop()
       display_students()
       
     
            

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    add_new_name = input( "name:")
    
    #TODO Check if the student is in the list, then ask for the new name
    if add_new_name in students:
        index = students.index(add_new_name)
        new_name = input("new name:")
    #TODO Update the student's name in the list
        students[index] = new_name
    #TODO If the student is not found, print an error message
    else:
        print("no student")
    #TODO display the updated list
    display_students()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1" :
            add_student()
        elif choice == "2" :
            remove_student()
        elif choice == "3" :
            pop_student()
        elif choice == "4" :
            update_student()
        elif choice == "5" :
            break
        else:
            print("incorrect choice")
            
        

        #TODO depending of the user choice option (1 - 5), call the correct function

# Start the program
menu()