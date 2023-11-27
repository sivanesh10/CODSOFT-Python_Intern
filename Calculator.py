from tkinter import *
main = Tk()
main.title("Calculator")
main.geometry("200x200")
var = StringVar()

label_1 = Label(main, text='Enter First No:')
label_1.grid() 
label_2 = Label(main, text='Enter Second No:')
label_2.grid() 

entry_1 = Entry (main, width=10)
entry_1.grid()
entry_2 = Entry(main, width=10)
entry_2.grid()


operator_var = StringVar()
operator_var.set("+") 

operator_label = Label(main, text="Operator:")
operator_label.grid()
operator_dropdown = OptionMenu(main,operator_var, "+", "-", "*", "/")
operator_dropdown.grid()

def calculator():

    first_number = entry_1.get()

    second_number = entry_2.get()

    symbol = operator_var.get()

    if symbol == "+":
        result_label.set(int(first_number) + int(second_number))
    
    elif symbol == "-":
      result_label.set(int(first_number) - int(second_number))
    
    elif symbol == "*":
        result_label.set(int(first_number) * int(second_number))
    
    elif symbol =="/":
        result_label.set(int(first_number) / int(second_number))

result_button = Button(main,text="result",anchor = "s",command=calculator)
result_button.grid()
result_label = StringVar()

Label(main,textvariable=result_label).grid()

main.mainloop()
