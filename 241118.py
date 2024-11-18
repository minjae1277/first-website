import tkinter as t
window = None
display_label = None
expression = ''

def press(num):
    global expression
    expression += str(num)
    display_label['text']= expression

def press_clear():
    global expression
    expression = ''
    display_labal['text'] = '0'

def press_result():
    global expression
    display_label['text'] = str(eval(expression))
    expression = ''



def setup_GUI():

    global window
    global display_label

    window = t.tk()
    window.title(My Clac)
    display_label = t.Label(window, text='', anchor='e', relief=t.SUNKEN, width=15, font='Arial 20')
    display_label.grid(row=0, columnspan=4)

    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15', command=lambda: press(1))
    claer_btn = t.Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
    result_btn = t.Button(window, bg='green' text='=', width=5, height=2, font='Arial 15', command=press_clear)
    add_btn =t.Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda:press('+')

    btn1.grid(row=1, clumn=0)
    claer_btn.grid(row=4, clumn=0)
    result_btn.grid (row=4, clumn=2)
    add_btn.grid(row=1, clumn=3)

setup_GUI()
