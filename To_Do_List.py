def exit_button():
    window.destroy()


def del_list():
    text.delete("1.0","end")


def put_list():
    global string
    string = entry_1.get()
    global l
    l = []
    l.append(string)
    entry_1.delete(0,END)
    printing(l)

def printing(a):
    k = "#"
    i = 0
    text.insert(END,f"[{k}] ")
    flag = True
    while flag:
        if len(a) > 0 :
                try:
                    text.insert(END,f"  {a[i]}\n")
                    i+=1
                except:
                    break
                try:
                    if a[i+1] in a:
                            flag = True
                except:
                    False

from tkinter import *
window = Tk()
window.geometry("400x700")
window.title("To_Do_List")
window.configure(background="lightgreen")


entry_1 = Entry(window,text="Enter the list",width="50")
entry_1.place(height="40")
entry_1.pack(ipady="40",ipadx="30")


button_1 = Button(window,text="Add",background="red",width="30",command=put_list)
button_1.place(height="30",width="100",x="150",y="120")

label_3 = Label(window,text="Click here to delete",justify="center",font=("Times",24,"underline"),background="pink")
label_3.config(background="pink")
label_3.place(x="80",y="180")


button_del = Button(window,background="red",text="Delete",command=del_list,width=20)
button_del.place(x="130",y="270")


button_exit = Button(window,text="Exit",background="red",command=exit_button,width=30)
button_exit.place(x="90",y="330")


welcome_label = Label(window,text="Welcome Users!!!",font=("Times",24,"underline"),justify="center",background="pink")
welcome_label.place(x="80",y="390")


text = Text(window)
text.place(x="30",y="480",width="340",height="180")


window.mainloop()

    

