from tkinter import *
root = Tk()

root.geometry("500x300")
root.title("Username & Password")

username = StringVar()
password = StringVar()

lab1 = Label(root, text = "Please Enter Username:")
lab1.place(x=50, y=10)
ent1 = Entry(root)
ent1.place(x=250, y=10)

lab2 = Label(root, text = "Please Enter Password:")
lab2.place(x=50, y=50)
ent2 = Entry(root, show="*")
ent2.place(x=250, y=50)

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)

def exit():
    root.destroy()

def log():
    from tkinter import messagebox
    username = ["Ayyoob", "Abdul", "Nathan", "Matthew", "Zipho"]
    password = ["0000", "5555", "7700", "1234", "9621"]
    found = False

    for x in range(len(username)):
        if ent1.get() == username[x] and ent2.get() == password[x]:
            found = True

    if found == True:
        messagebox.showinfo("STATUS","Access Granted!")
        root.destroy()
        import selection_sort_tkinter

    else:
        messagebox.showinfo("ERROR INFO","Access Denied!")

btn1 = Button(root, text = "LogIn", borderwidth = "10", command = log)
btn1.place(x=20, y=150)

btn2 = Button(root, text = "Clear", borderwidth = "10", command = clear)
btn2.place(x=120, y=150)

btn3 = Button(root, text = "Exit", borderwidth = "10", command = exit)
btn3.place(x=230, y=150)


root.mainloop()
