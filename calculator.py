from tkinter import *
root=Tk()
root.title("calculator")
#root.iconbitmap("calculator.ico")

root.resizable(False,False)

frame=Frame(root)
frame.grid(row=0,column=0,columnspan=5)

equation=StringVar()
equation.set("0")

e=Entry(frame,textvariable=equation,justify="right",font=("bold",23))
e.grid(row=0,column=0)

expression=""
def click_button(number):
    global expression
    expression=expression+str(number)
    equation.set(expression)

def clear_button():
    global expression
    length=len(e.get())
    e.delete(length-1,END)
    expression=e.get()
    global h
    h=expression

def clear1_button():
    global expression
    e.delete(0,END)
    expression=""

def history_button():
    try:
        equation.set(h)

    except:
        equation.set("No history is available")

def equal_button():
    try:
            global expression
            global h
            h=expression
            total=str(eval(expression))
            equation.set(total)
            expression=total
            total = str(eval(expression))
            equation.set(total)

    except:
        equation.set("error")
        expression=""


button1=Button(root,text="1", padx=35, pady=18, font="bold", command=lambda: click_button(1))
button2=Button(root,text="2", padx=35, pady=18, font="bold", command=lambda: click_button(2))
button3=Button(root,text="3", padx=35, pady=18,  font="bold", command=lambda: click_button(3))
button4=Button(root,text="4", padx=35, pady=18, font="bold", command=lambda: click_button(4))
button5=Button(root,text="5", padx=35, pady=18, font="bold", command=lambda: click_button(5))
button6=Button(root,text="6", padx=35, pady=18, font="bold", command=lambda: click_button(6))
button7=Button(root,text="7", padx=35, pady=18, font="bold", command=lambda: click_button(7))
button8=Button(root,text="8", padx=35, pady=18, font="bold", command=lambda: click_button(8))
button9=Button(root,text="9", padx=35, pady=18, font="bold", command=lambda: click_button(9))
button0=Button(root,text="0", padx=35, pady=18, font="bold", command=lambda: click_button(0))
decimal=Button(root,text=".", padx=37.5, pady=18, font="bold", command=lambda: click_button('.'))
clear1=Button(root,text="C", padx=82, pady=18, font="bold",command=clear1_button)
clear=Button(root,text="CE", padx=28.49, pady=18, font="bold", command=clear_button)
equal=Button(root,text="=", padx=36, pady=55, font="bold", command=equal_button)
subtract=Button(root,text="-", padx=36.5, pady=18,font="bold",command=lambda: click_button('-'))
multiply=Button(root,text="*", padx=38, pady=18, font="bold", command=lambda: click_button('*'))
divide=Button(root,text="/", padx=39.1, pady=18, font="bold", command=lambda: click_button('/'))
mod=Button(root,text="%", padx=31, pady=18, font="bold", command=lambda: click_button('%'))
bracket1=Button(root,text="(", padx=37, pady=18, font="bold", command=lambda: click_button('('))
bracket2=Button(root,text=")", padx=37, pady=18, font="bold", command=lambda: click_button(')'))
add=Button(root,text="+", padx=36, pady=18, font="bold",command=lambda:click_button('+'))
history=Button(root,text="History", padx=10, font="bold", pady=18,command=history_button)


bracket1.grid(row=1, column=0)
bracket2.grid(row=1, column=1)
mod.grid(row=1, column=2)
clear.grid(row=1, column=3)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
add.grid(row=2, column=3)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
divide.grid(row=3, column=3)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
multiply.grid(row=4, column=3)
button0.grid(row=5, column=0)
decimal.grid(row=5, column=1)
subtract.grid(row=5, column=2)
equal.grid(row=5, column=3,rowspan=2)
history.grid(row=6, column=0)
clear1.grid(row=6, column=1,columnspan=2)

root.mainloop()



