import tkinter

def display_grade():
    user_input =entry.get().upper()
    if user_input =="O":
        label2.config(text="Outstandig")
    elif user_input =="A":
        label2.config(text="Very Good")
    elif user_input =="B":
        label2.config(text ="Good")
    elif user_input =="C":
        label2.config(text="Average")
    elif user_input =="F":
        label2.config(text="Fail")
    else:
        label2.config(text="Invalid Grade")
        
        
root = tkinter.Tk()
root.geometry("400x400")
root.title("Grades Display")

label1 = tkinter.Label(root, text="Enter Grade(O,A,B,C, OR F)")
label1.pack()


entry = tkinter.Entry(root, width=10)
entry.pack()

buttom = tkinter.Button(root, text="Submit", command=display_grade)
buttom.pack()

label2 = tkinter.Label(root, text="")
label2.pack      

root.mainloop()

        
        








