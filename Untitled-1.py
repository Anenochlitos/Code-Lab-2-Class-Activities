from tkinter import *

root=Tk()
root.title("Tkinter")
root.geometry("400x600")
root.resizable(0,0)
root.configure(bg="black")

Introname = Label(root,text="Hallu, my name is y",
                  width=20)
School = Label(root,text="I'm from Ras Al Kaimah, Bathspa University",
               width=20)
Age = Label(root, text= "I'm old enough to work",
            width=20,)
Favcolor = Label(root, text="I like orange",
            fg="orange",
            width=20)
Favcolor2 = Label(root,text="My second favorite color is blue",
            bg="blue",
            width=20)
Font = Label(root,text= "I like the font Roboto",
            font=('Roboto', 25),
            height=2,
            width =20)

Height = Label(root,text="My height is 6'7",
               height=67,
               width=20,)

Introname.pack()
School.pack()
Age.pack()
Favcolor.pack()
Favcolor2.pack()
Font.pack(pady=20)
Height.pack()

root.mainloop()
