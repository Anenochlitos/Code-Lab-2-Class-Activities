from tkinter import *

root = Tk()
Label(root, text="Check buttons to select multiple options").pack(anchor=W)
c1 =Checkbutton(root, text="Homosexual").pack(anchor=W)
c2 =Checkbutton(root, text="Bisexual").pack(anchor=W)
Label(root, text="Radio buttons to select one option").pack(anchor=W)
r1 = Radiobutton(root, text="Son of God", value=1).pack(anchor=W)
r2 = Radiobutton(root, text="Christian", value=2).pack(anchor=W)
r3 = Radiobutton(root, text="")