from tkinter import *
import sqlite3

def employee():
    window = Tk()

    window.mainloop()


def checkemp():
    conn = sqlite3.connect("employe.db")
    c = conn.cursor()
    c.execute("SELECT username FROM login WHERE username=? AND password=?", (entry_e1.get(), entry_e2.get()))
    if c.fetchone():
       main.destroy()
       employee()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        rlbl.pack()
        r.mainloop()


def loginemp():
    main.destroy()
    global entry_e1
    global entry_e2
    root = Tk()
    root.title('Employee Login')

    label_e1 = Label(root, text='Username/ID', anchor=E)
    label_e1.grid(row=0)
    label_e2 = Label(root, text='Password', anchor=E)
    label_e2.grid(row=1)

    entry_e1 = Entry(root)
    entry_e1.grid(row=0, column=1)
    entry_e2 = Entry(root, show='*')
    entry_e2.grid(row=1, column=1)

    button_e1 = Button(root, text='Login', command=checkemp)
    button_e1.grid(row=2)

    root.mainloop()


main = Tk()
main.title('Login')

label_1 = Label(main, text='Login as:', anchor=N)
label_1.grid(row=0)

button_2 = Button(main, text='Employee', command=loginemp)
button_2.grid(row=1)

main.mainloop()
