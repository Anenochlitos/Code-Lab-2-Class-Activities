from tkinter import *

root=Tk()

root.geometry("300x300")
root.title("Working with images")

img = PhotoImage(file="Border.png")

label =Label(root, image=img)
label.pack()

root.mainloop()
