from tkinter import *
from tkinter import messagebox
root1 = Tk()
root1.geometry("600x400+0+0")
root1.title("easy question")



def ent1():
    f = open('temp.txt' ,'a')
    f.write('1')
    f.close
    messagebox.showinfo('Acknowledgement', 'your ans is correct.')

    root1.destroy()
    import easy5

def ent2():
    messagebox.showinfo('Acknowledgement', 'your ans is wrong.The correct ans is option (a).')
    root1.destroy()
    import easy5


label = Label(root1, font=('arial', 40, 'bold'), text="4.Who is a cricketer?", fg="black", bd=20, anchor='w')
label.grid(row=0)

btn1=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="SACHIN    ",bg="blue"
            ,command=ent1 )
btn1.grid(row=2,column=0)

btn2=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="KAPIL       ",bg="pink"
            ,command=ent2 )
btn2.grid(row=3,column=0)

btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="KEJRIWAL",bg="powder blue"
            ,command=ent2)
btn3.grid(row=4,column=0)
btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="PANKAJ    ",bg="powder blue"
            ,command=ent2)
btn3.grid(row=5,column=0)

root1.mainloop()