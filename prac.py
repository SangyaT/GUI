#!/usr/bin/env python

from tkinter import *
import ttk
from ttk import * 

i =2

def add_row():
    global i 
    var = IntVar()
    c = Checkbutton(root, variable = var)
    c.grid(row = i, column = 0)
    for j in range(1,5): #Columns

            b = Entry(root)
            b.grid(row=i, column=j)
    i =i+1 

root = Tk()
bt = ttk.Button(root , text = 'Add Row', command = add_row)
bt.grid(row =0, column=0)


dl = ttk.Button(root , text = 'Delete Row')
dl.grid(row =0, column=1)

v0 = StringVar()
e0 = Entry(root, textvariable = v0, state = 'readonly')
v0.set('Select')
e0.grid(row = 1, column = 0 )

v1 = StringVar()
e1 = Entry(root, textvariable = v1, state = 'readonly')
v1.set('Col1')
e1.grid(row = 1, column = 1 )

v2 = StringVar()
e2 = Entry(root, textvariable = v2, state = 'readonly')
v2.set('Col2')
e2.grid(row = 1, column = 2)

v3 = StringVar()
e3 = Entry(root, textvariable = v3, state = 'readonly')
v3.set('Col3')
e3.grid(row = 1, column = 3 )

v4 = StringVar()
e4 = Entry(root, textvariable = v4, state = 'readonly')
v4.set('Col4')
e4.grid(row = 1, column = 4 )

mainloop()
