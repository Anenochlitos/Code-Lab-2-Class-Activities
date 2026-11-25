from tkinter import *

glute = Tk()
glute.title("My First GLUTE")
glute.geometry("400x400")
Label(glute, text="Smash my gyatt", font=('Roboto', 25)).pack()
Label(glute, text="Whose gyatt is better?", font=('Roboto', 10)).pack(side=RIGHT)
Button(glute, text="My Gyatt").pack(side=LEFT, expand=YES, fill=Y)
Button(glute, text="Nathan's Gyatt").pack(side=TOP, expand=YES, fill=BOTH)
Radiobutton(glute, text="Mine?", value=1).pack(side=RIGHT)

nathangyatt = Radiobutton(glute, text="Nathan's?", value=2)
nathangyatt.pack(side=RIGHT)



glute.mainloop()