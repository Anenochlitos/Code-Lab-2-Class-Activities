from tkinter import *

christian = Tk()
christian.title("Christian's GUI")

Label(christian, text="Hello, World!").pack(side=TOP)
Label(christian, text="Are u a christian?").pack(expand=Y)
Entry(christian).pack(fill=X)

christian.mainloop()

