from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except Exception as e:
        equation.set("ERROR: " + str(e))
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("510x460")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=19, ipadx=190)

    btn1 = Button(gui, text='1', fg='black', bg='red', command=lambda: press(1), height=5, width=15)
    btn1.grid(row=2, column=0)
    btn2 = Button(gui, text='2', fg='black', bg='red', command=lambda: press(2), height=5, width=15)
    btn2.grid(row=2, column=1)
    btn3 = Button(gui, text='3', fg='black', bg='red', command=lambda: press(3), height=5, width=15)
    btn3.grid(row=2, column=2)
    btn4 = Button(gui, text='4', fg='black', bg='red', command=lambda: press(4), height=5, width=15)
    btn4.grid(row=3, column=0)
    btn5 = Button(gui, text='5', fg='black', bg='red', command=lambda: press(5), height=5, width=15)
    btn5.grid(row=3, column=1)
    btn6 = Button(gui, text='6', fg='black', bg='red', command=lambda: press(6), height=5, width=15)
    btn6.grid(row=3, column=2)
    btn7 = Button(gui, text='7', fg='black', bg='red', command=lambda: press(7), height=5, width=15)
    btn7.grid(row=4, column=0)
    btn8 = Button(gui, text='8', fg='black', bg='red', command=lambda: press(8), height=5, width=15)
    btn8.grid(row=4, column=1)
    btn9 = Button(gui, text='9', fg='black', bg='red', command=lambda: press(9), height=5, width=15)
    btn9.grid(row=4, column=2)
    btn0 = Button(gui, text='0', fg='black', bg='red', command=lambda: press(0), height=5, width=15)
    btn0.grid(row=5, column=0)

    plus = Button(gui, text='+', fg='black', bg='red', command=lambda: press('+'), height=5, width=15)
    plus.grid(row=2, column=3)
    minus = Button(gui, text='-', fg='black', bg='red', command=lambda: press('-'), height=5, width=15)
    minus.grid(row=3, column=3)
    mult = Button(gui, text='*', fg='black', bg='red', command=lambda: press('*'), height=5, width=15)
    mult.grid(row=4, column=3)
    div = Button(gui, text='/', fg='black', bg='red', command=lambda: press('/'), height=5, width=15)
    div.grid(row=5, column=3)

    eq = Button(gui, text='=', fg='black', bg='red', command=equalpress, height=5, width=15)
    eq.grid(row=5, column=2)
    clr = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=5, width=15)
    clr.grid(row=5, column=1)
    dot = Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=5, width=15)
    dot.grid(row=6, column=0)


    gui.mainloop()