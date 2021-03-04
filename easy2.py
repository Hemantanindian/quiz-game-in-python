from tkinter import *
from tkinter import messagebox
root1 = Tk()
root1.geometry("400x400+0+0")
root1.title("easy question")



def ent1():
    f = open('temp.txt' ,'a')
    f.write('1')
    f.close
    messagebox.showinfo('Acknowledgement', 'your ans is correct.')

    root1.destroy()
    import easy3

def ent2():
    messagebox.showinfo('Acknowledgement', 'your ans is wrong.The correct ans is option (b).')
    root1.destroy()
    import easy3


label = Label(root1, font=('arial', 40, 'bold'), text="2.)  5+8+3 = ?", fg="black", bd=20, anchor='w')
label.grid(row=0)

btn1=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="15",bg="blue"
            ,command=ent2 )
btn1.grid(row=2,column=0)

btn2=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="16",bg="pink"
            ,command=ent1 )
btn2.grid(row=3,column=0)

btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="17",bg="powder blue"
            ,command=ent2)
btn3.grid(row=4,column=0)
btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="18",bg="powder blue"
            ,command=ent2)
btn3.grid(row=5,column=0)

root1.mainloop()