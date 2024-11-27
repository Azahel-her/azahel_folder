import tkinter

x = tkinter.Tk()
x.title("AZAWORK2")

menu1 = tkinter.Menu(x)
x.config(menu=menu1)
filemenu = tkinter.Menu(menu1, tearoff=0)
menu1.add_cascade(label="Edit", menu=filemenu)
filemenu.add_command(label= "Cut")
filemenu.add_command(label="Copy")
filemenu.add_separator()
filemenu.add_command(label = "Paste")


x.mainloop()