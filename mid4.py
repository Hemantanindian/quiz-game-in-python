from tkinter import *
from tkinter import messagebox
root1 = Tk()
root1.geometry("600x400+0+0")
root1.title("middium question")



def ent1():
    f = open('temp.txt','a')
    f.write('1')
    f.close
    messagebox.showinfo('Acknowledgement', 'your ans is correct.')

    root1.destroy()
    import mid5

def ent2():
    messagebox.showinfo('Acknowledgement', 'your ans is wrong.The correct ans is option (D).')
    root1.destroy()
    import mid5


label = Label(root1, font=('arial', 20, 'bold'), text="4.In which state main language khasi?", fg="black", bd=20, anchor='w')
label.grid(row=0)

btn1=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="MIZORAM     ",bg="blue"
            ,command=ent2 )
btn1.grid(row=2,column=0)

btn2=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="NAGALAND  ",bg="pink"
            ,command=ent2 )
btn2.grid(row=3,column=0)

btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="TRIPURA      ",bg="powder blue"
            ,command=ent2)
btn3.grid(row=4,column=0)
btn3=Button(root1,padx=1,pady=1,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="MEGHALAYA",bg="plum"
            ,command=ent1)
btn3.grid(row=5,column=0)

root1.mainloop()