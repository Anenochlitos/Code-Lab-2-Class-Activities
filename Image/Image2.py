from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.geometry("3000x3000")
root.title("Working with images")

img = ImageTk.PhotoImage(file="DSCF4936.jpeg")

label =Label(root, image=img)
label.pack(fill=BOTH, expand=True)

root.mainloop()