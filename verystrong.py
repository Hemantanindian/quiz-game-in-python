from tkinter import*
root = Tk()
root.geometry("800x400+0+0")
root.configure(background="bisque")
root.title("result")

def start():
    root.destroy()
    import home

def exit():
    root.destroy()
    exit()



lblinfo = Label(root, font=( 'aria', 30, 'bold' ), text="You give all the correct answer.",fg="steel blue", bg="bisque", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(root, font=( 'aria', 30, 'bold' ), text="You have very strong general knowledge",fg="steel blue", bg="bisque", bd=10, anchor='w')
lblinfo.grid(row=1, column=0)

b = Button(root, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="start again", bg="blue", command=start)
b.place(relx=0.7, rely=0.7, anchor=CENTER)
b1 = Button(root, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="exit", bg="blue", command= exit)
b1.place(relx=0.3, rely=0.7, anchor=CENTER)
root.mainloop()