import tkinter as tk
from tkinter import ttk


def callbackFunc(event):
    print("New Element Selected")
    print(comboExample.get())
    comboExample.configure(font=comboExample.get())


app = tk.Tk()
app.geometry('200x100')


labelTop = tk.Label(app,
                    text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app,
                            values=["Arial",
                                    "Algerian",
                                    "STXingkai",
                                    "French Script MT"])


comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


app.mainloop()
