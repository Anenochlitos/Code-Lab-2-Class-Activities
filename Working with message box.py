from tkinter import *
import tkinter.messagebox
from tkinter import messagebox

root = Tk()
root.title("Working with message box")
root.geometry("400x400")
root.config(bg="lightblue")

b1 = Button(root, text="Show Info", 
            fg="white", bg="green", font=("Arial", 14), 
            command=lambda: messagebox.showinfo("Info", "This is an info message"))
b1.place(x=100, y=50)

b2 = Button(root, text="Yes or No", 
            fg="white", bg="orange", font=("Arial", 14), 
            command=lambda: messagebox.askyesno("Question", "Do you want to continue?"))
b2.place(x=100, y=100)

l1 = Label(root, text="", bg="lightblue", font=("Arial", 14))
l1.place(x=100, y=200)

def clickhere():
    messagebox.showinfo("Successful", "You clicked the button!")
def click():
    answer = messagebox.askyesno("Confirmation", "Continue?")
    if answer:
        l1.config(text="Confirmed")
    else:
        l1.config(text="Cancelled")

root.mainloop()