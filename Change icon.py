from tkinter import *
from PIL import Image, ImageTk

main = Tk()
main.title("Student Management System")
main.geometry("350x600")
main.resizable(0,0)
main.iconbitmap("icons8-business-conference-50.ico.png")

img = ImageTk.PhotoImage(Image.open("girl.jpg"))

Label(main, image=img).place(x=0, y=0)

label_frame = Frame(main, bg="white")
label_frame.place(x=0, y=115, width=350, height=125)

Name = Label(label_frame, text="Student \n Management \n System", 
             font=("times new roman", 25, "bold"), bg="white", fg="green")
Name.place(relx=0.5, rely=0.5, anchor=CENTER)

pic1 = Image.open("girl.jpg")
pic1 = pic1.resize((30, 30))

button= Button(main, image=ImageTk.PhotoImage(pic1), 
               text="Add Student", compound=LEFT, 
               font=("times new roman", 15, "bold"), 
               bg="green", fg="white", bd=0, 
               cursor="hand2").place(x=50, y=300, width=250, height=40)

main.mainloop()