from tkinter import *

top = Tk()
top.title('find & replace')
Label(top, text="Find:").grid(row=0, column=0, stick='e')
Label(top, text="Replace:").grid(row=1, column=0, sticky='e')

Entry(top).grid(row=0, column=1, padx=2,pady=2,stick='we', columnspan=9)
Entry(top).grid(row=1, column=1, sticky='ew', padx=2,pady=2, columnspan=9)

Button(top, text="Find").grid(row=0, column=10, sticky='ew', padx=2, pady=2)
Button(top, text="Find All",).grid(row=1, column=10, sticky='ew', padx=2)

Button(top, text="Replace").grid(row=2, column=10, sticky='ew', padx=2)
Button(top, text="Replace All").grid(row=3, column=10, sticky='ew', padx=2)

Checkbutton(top, text="Match whole word only").grid(row=2,column=1,columnspan=4,sticky='w')
Checkbutton(top, text="Match case").grid(row=3,column=1,columnspan=4,sticky='w')




top.mainloop()