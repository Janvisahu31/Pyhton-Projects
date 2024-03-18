from tkinter import *
import random

def click1(event):
    global strval3
    global strval
    global strval2
    s=random.randint(1,4)
    if(s==1):
        strval3="its a tie"
    elif s==2:
        strval3="you lose"
        value=int(strval)

        
        strval=value+1
        screen.update()
    else:
        strval3="you win"
        value=int(strval2)
        
        strval2=value+1
        screen.update()
    screen3.update
        
        
        
        
        

root=Tk()
root.geometry("550x700")
root.minsize(550,700)
root.maxsize(550,700)


root.title("stonePaperScissiors")



f=Frame(root,bg="grey")
strval=StringVar()
strval.set("0")
screen=Entry(f,textvar=strval,font="sans 50 bold",width=5)
screen.pack(padx=1,side=LEFT)
lable=Label(f,text=":",font="sans 50 bold")
lable.pack(side=LEFT)
strval2=StringVar()
strval2.set("0")
screen1=Entry(f ,textvar=strval2,font="sans 50 bold",width=5)
screen1.pack(padx=1,side=LEFT)
f.pack(padx=10)


l=Label(root,text="Choose your move",font="sans 20 bold")
l.pack()


f1=Frame(root,bg="grey")
b1=Button(f1,text="STONE",font="sans 30 bold",padx=5,pady=20)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click1)
b2=Button(f1,text="PAPER",font="sans 30 bold",padx=5,pady=20)
b2.pack(side=LEFT)
b2.bind("<Button-1>",click1)
b3=Button(f1,text="SCISS",font="sans 30 bold",padx=7,pady=20)
b3.pack(side=LEFT)
b3.bind("<Button-1>",click1)
f1.pack(fill=X,padx=10)

strval3=StringVar()
strval3.set("")
screen3=Entry( root,textvar=strval3,font="sans 50 bold")
screen3.pack(fill=X,ipadx=8,pady=10,padx=10)
