from tkinter import *
import time
from tkinter import messagebox


def easy():
    root.destroy()
    import easy1

def medium():
    root.destroy()
    import mid1


def hard():
    root.destroy()
    import hard1


root =Tk()
root.geometry("500x350")
root.title("time counter")
btn1=Button(root,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="EASY    ",bg="blue"
            , )

lblinfo = Label(root, font=('aria', 18, ), text="PLEASE SELECTYOUR LEVEL OF QUIZ.", bg="bisque", fg=         "darkred", anchor=W)
lblinfo.grid(row=2, column=0)

btn1=Button(root,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="EASY    ",bg="blue"
            ,command=easy )
btn1.grid(row=8,column=0)

btn2=Button(root,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="MEDIUM",bg="pink"
            ,command=medium )
btn2.grid(row=9,column=0)

btn3=Button(root,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="HARD    ",bg="powder blue"
            ,command=hard)
btn3.grid(row=10,column=0)
sec = StringVar()
Entry(root,textvariable = sec, width = 2, font = 'arial 12').place(x=100, y= 105)
sec.set("00")
temp = 30
while temp >=-1:
    sec.set("{0:2d}".format(temp))
    root.update()
    time.sleep(1)
    if (sec == 0):
        messagebox.showinfo("time countdown","time's up")
    temp -= 1
root.mainloop()