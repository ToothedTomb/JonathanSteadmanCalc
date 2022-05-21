#!/usr/bin/env python3
from tkinter import*
import tarfile
import os
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
cal = tk.Tk()
my_menu=Menu(cal)
cal.config(menu=my_menu,background="#90ee90")
def our_command():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("What is this software?")

    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software?")
    label = tk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This is a free and open source calculator for Linux and FreeBSD.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="green",border=12,activebackground='orange', command = root.destroy)
    B1.pack()
def our_command2():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("Who made this software?")

    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this software?")
    label = tk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="green",border=12,activebackground='orange', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,background="#90ee90")
my_menu.add_cascade(label="About:",font=("Ubuntu",18),activebackground="#90ee90", menu=file_menu)
file_menu.add_command(label="What is this software?",font=("Ubuntu",18),activebackground="#90ee90",command=our_command)
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="#90ee90",command=our_command2)

cal.title("Basic Calculator 8.0!")
cal.tk.call('wm', 'iconphoto', cal._w, tk.PhotoImage(file='icons.png'))
cal.resizable(0,0)
cal.config(bg='#90ee90')
operator=""
text_Input =StringVar()
def btnEqualsInput():
    global oper6ator
    sumup=str(eval(operator))
    text_Input.set(sumup)

def on_enter(e):
   btn7.config(background='OrangeRed3', foreground= "white")
operator=""
txtDisplay = Entry(cal,font=('Ubuntu', 30), textvariable=text_Input, bd=30, insertwidth=4,
bg="#90ee90", justify='left').grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="7", bg="green",activebackground='orange',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="8", bg="green",activebackground='orange',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="9", bg="green",activebackground='orange',command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="+", bg="green",activebackground='orange',command=lambda:btnClick("+")).grid(row=1,column=3)
#======================================================================
btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="4", bg="green",activebackground='orange',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="5", bg="green",activebackground='orange',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="6", bg="green",activebackground='orange',command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="-", bg="green",activebackground='orange', command=lambda:btnClick("-")).grid(row=2,column=3)
#======================================================================
btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="1", bg="green",activebackground='orange',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="2", bg="green",activebackground='orange',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="3", bg="green",activebackground='orange',command=lambda:btnClick(3)).grid(row=3,column=2)
Mutiply=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="*", bg="green",activebackground='orange',command=lambda:btnClick("*")).grid(row=3,column=3)
#======================================================================
btn0=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="0", bg="green",activebackground='orange',command=lambda:btnClick(0)).grid(row=4,column=0)
Division=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="/", bg="green",activebackground='orange',command=lambda:btnClick("/")).grid(row=4,column=1)
btnEquals=Button(cal,padx=16, pady=16, bd=8, fg="black",font=('Ubuntu',24,'bold'),
text="=", bg="#3b8eea",activebackground='orange',command=btnEqualsInput).grid(row=4,column=3)
btnClear=Button(cal,padx=16, pady=16, bd=8, fg="black",font=('Ubuntu',28,'bold'),
text="C", bg="green", activebackground='orange',command= btnClearDisplay).grid(row=4,column=2)

#=======================================================================
#When the user try to close the software. They will see this message. Press okay to close.
#To cancel press cancel. 
def on_closing():
    if messagebox.askokcancel("Confirm to exit the software:", "Are you sure you want to exit?"):
        cal.destroy()
cal.protocol("WM_DELETE_WINDOW", on_closing)
cal.mainloop() 
#