import tkinter as tk

from tkinter import *
from tkinter import ttk
root = Tk()
root.title('calculator')
root.geometry("370x620+100+200")
root.resizable(False, False)
root.configure(bg="#000000")
equation = ''
def show(value):
     global equation
     equation+=value
     label_result.config(text=equation)
def clear():
    global equation
    equation = ''
    label_result.config(text=equation)
def calculate():
    global equation
    result = ''
    if equation != "":
        try:
            result =eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)






label_result = Label(root, width=25, height=2,text="", font=("arial", 30))
label_result.pack()
Button(root, width=3, height=1,text="C", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#FF0000', command=lambda: clear()).place(x=10, y=100)
Button(root, width=3, height=1,text="%", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('%')).place(x=100, y=100)
Button(root, width=3, height=1,text="", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('')).place(x=190, y=100)
Button(root, width=3, height=1,text="/", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('/')).place(x=280, y=100)

Button(root, width=3, height=1,text="7", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('7')).place(x=10, y=200)
Button(root, width=3, height=1,text="8", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('8')).place(x=100, y=200)
Button(root, width=3, height=1,text="9", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('9')).place(x=190, y=200)
Button(root, width=3, height=1,text="-", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('-')).place(x=280, y=200)

Button(root, width=3, height=1,text="4", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('4')).place(x=10, y=300)
Button(root, width=3, height=1,text="5", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('5')).place(x=100, y=300)
Button(root, width=3, height=1,text="6", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('6')).place(x=190, y=300)
Button(root, width=3, height=1,text="+", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('+')).place(x=280, y=300)

Button(root, width=3, height=1,text="1", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('1')).place(x=10, y=400)
Button(root, width=3, height=1,text="2", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('2')).place(x=100, y=400)
Button(root, width=3, height=1,text="3", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('3')).place(x=190, y=400)
Button(root, width=3, height=1,text="=", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: calculate()).place(x=280, y=400)

Button(root, width=7, height=1,text="0", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('0')).place(x=10, y=500)
Button(root, width=7, height=1,text=".", font=("arial", 30, 'bold'), bd=1, fg='#fff', bg='#606060', command=lambda: show('.')).place(x=190, y=500)
root.mainloop()