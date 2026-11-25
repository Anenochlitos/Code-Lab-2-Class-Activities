from tkinter import *

regist = Tk()
regist.title("Registration Form")

Label(regist, text="Username").grid(row=0, column=0)
Entry(regist).grid(row=0, column=1)
Label(regist, text="Password").grid(row=1, column=0)
Entry(regist, show="*").grid(row=1, column=1)
regist.mainloop()