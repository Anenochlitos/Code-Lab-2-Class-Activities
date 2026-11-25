from tkinter import *

root = Tk()
root.title("The lord is my shepherd")
root.geometry("400x600")
root.resizable(0, 0)
root.configure(bg="black")

Top = Label(root, text="",
            height=10,
            width=17)
Middle = Label(root, text="The lord is my shepherd",
               font=('Roboto', 25),
               height=2,
               width=21)
Bottom = Label(root, text="",
               height=67,
               width=17)

Top.pack()
Middle.pack(pady=10)
Bottom.pack()

root.mainloop()
