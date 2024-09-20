from tkinter import *

def add():
    global strval
    a=screen.get()
    lbx.insert(END,a)

def delete():
    lbx.delete(ANCHOR)

first_root= Tk()
#gui logic here
first_root.geometry("1200x1200")

first_root.maxsize(1200,1200)





f1=Frame(first_root,borderwidth=8,bg="red",relief=RIDGE)
f1.pack(side=TOP,fill="x")

f2=Frame(first_root,borderwidth=1,bg="pink",relief=GROOVE)
f2.pack(side=LEFT,fill="y")





title_lable=Label(f1,text="To do List",font=" Comicsans 100 bold",borderwidth=3,background="red")
title_lable.pack()


lable2=Label(f2,text="Tasks",font=" Comicsans 40 bold",borderwidth=3,background="pink")
lable2.pack(padx=300)
f3=Frame(first_root,borderwidth=4,relief=GROOVE)
lable3=Label(f3,text="Choose your option",font=" Comicsans 20 bold",borderwidth=3,background="pink")
lable3.pack(padx=80,pady=20)

but1= Button(f3,text="ADD task",font="Comicsans 20 bold",command=add)
but1.bind('<Double-1>',add)

but1.pack(padx=23,pady=23)

strval=StringVar()
strval.set("")
screen=Entry(f3,textvar=strval,font="sans 20 bold",width=25)
screen.pack(padx=1)



but3= Button(f3,text="Delete task",font="Comicsans 20 bold",command=delete)
but1.bind('<Double-1>',delete)
but3.pack(padx=23,pady=23)

but4= Button(f3,text="close",font="Comicsans 30 bold")
but4.bind('<Double-1>',quit)
but4.pack(padx=23,pady=23)
f3.pack(side=RIGHT,fill="y")


lbx=Listbox(f2,width=80,height=40,font="Comicsans 10 bold")
lbx.pack()




first_root.mainloop()

