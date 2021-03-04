from tkinter import*

root = Tk()
root.geometry("800x600+0+0")
root.configure(background="bisque")
root.title("Quiz game :- By Hemant")
Tops = Frame(root, bg="bisque", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, bg="bisque", height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, bg="bisque", height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

f = open('temp.txt', 'w')
f.close

def start():
    root.destroy()
    import timer



lblinfo = Label(Tops, font=( 'aria', 30, 'bold' ), text="HELLO, WELCOME TO THE QUIZ.",fg="steel blue", bg="bisque", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=( 'aria', 18, 'bold' ), text="A LITTLE GAME TO TEST YOUR SKILLS AND KNOWLEDGE",fg="steel blue", bg="bisque", bd=10, anchor='w')
lblinfo.grid(row=1, column=0)
lblinfo = Label(Tops, font=('aria', 15, ), text="RULES:-                                ", bg="bisque", fg="black", anchor=W)
lblinfo.grid(row=3, column=0)
lblinfo = Label(Tops, font=('aria', 12, ), text="1.WE ASK 5 QUESTIONS.                    ", bg="bisque", fg="black", anchor=W)
lblinfo.grid(row=4, column=0)
lblinfo = Label(Tops, font=('aria', 12, ), text="2.EACH QUESTION HAVE 4 OPTION", bg="bisque", fg="black", anchor=W)
lblinfo.grid(row=5, column=0)
lblinfo = Label(Tops, font=('aria', 12, ), text="3.ONE OPTION IS CORRECT.             ", bg="bisque", fg="black", anchor=W)
lblinfo.grid(row=6, column=0)
lblinfo = Label(Tops, font=('aria', 12, ), text="4.YOU HAVE ONLY 30SEC.                 ", bg="bisque", fg="black", anchor=W)
lblinfo.grid(row=7, column=0)
lblinfo = Label(Tops, font=('aria', 18, ), text="\n", bg="bisque", fg="darkred", anchor=W)
lblinfo.grid(row=2, column=0)
lblinfo = Label(Tops, font=('aria', 18, ), text="\n\n\n\n", bg="bisque", fg="darkred", anchor=W)
lblinfo.grid(row=8, column=0)

btn1=Button(Tops,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="START",bg="blue"
            ,command=start)
btn1.grid(row=8,column=0)
root.mainloop()
