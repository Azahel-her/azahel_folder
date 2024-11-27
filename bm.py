import tkinter
def calculate():
    user_input= entry.get()
    user_input2 =entry2.get()
    
    x1 = bin(user_input)
    z1 = bin(user_input2)
    
    x = x1 * x1
    z = z1
    
    if x or z == True:
        result =z/x
    result = tkinter.Label(window,text="")
    result.pack(pady=10)    

window = tkinter.Tk()
window.title("BMI CALCULATOR")

instructions = tkinter.Label(window, text="Enter your height in meters:")
instructions.pack(pady=10)

entry = tkinter.Entry(window)
entry.pack(pady=10)

instructions = tkinter.Label(window, text="Enter your weight in kilograms:")
instructions.pack(pady=10)

entry2 = tkinter.Entry(window)
entry2.pack(pady=10)

button = tkinter.Button(window,text="Calculate BMI",command=calculate)
button.pack(pady=10)

result = tkinter.Label(window,text ="")
result.pack(pady=10)

window.mainloop()