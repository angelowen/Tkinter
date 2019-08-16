from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("hi")
root.geometry("300x180")
familyVar = StringVar()

def familychange(event):
    f = Font(family=familyVar.get())
    print(f)
    text.configure(font=f)

tup = ("Arial", "Times", "Courier")
familyVar.set(tup[2])
family = OptionMenu(root, familyVar, *tup, command=familychange)
family.pack()

text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.focus_set()

root.mainloop()