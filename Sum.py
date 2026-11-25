from tkinter import *
root = Tk()
root.title("Tkinter Program")
root.geometry("400x400")
root.config(bg="lightblue")

l1 = Label(root, text ="Enter Values",
           bg="lightblue", font=("Arial", 14))
l1.place(x=10, y=20)

e1 = Entry(root, font=("Arial", 14))
e1.place(width= 20,x=50, y=60)
e2 = Entry(root, font=("Arial", 14))
e2.place(width= 20,x=200, y=60)

l2 = Label(root, text ="",
           bg="lightblue", font=("Arial", 14))
l2.place(x=10, y=80)

def add():
    v1= int(e1.get())
    v2= int(e2.get())
    result = v1 + v2
    l2.config(text = f"Sum of two numbers is: {result}")

def sub():
    v1= int(e1.get())
    v2= int(e2.get())
    result = v1 - v2
    l2.config(text = f"Difference of two numbers is: {result}")

#Create button
#Sum
Button(root, text= "Sum", fg="white", bg="green", font=("Arial", 14), command=add).place(x=60, y=120)
#Subtract
Button(root, text= "Subtract", fg="white", bg="red", font=("Arial", 14), command=sub).place(x=200, y=120)

root.mainloop()