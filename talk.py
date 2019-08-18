import tkinter as tk
from functools import partial
import tkinter.messagebox
cnt = 0
window = tk.Tk()
window.title("communication")
window.geometry("600x600")
myfile = "talkfile.txt"


def see_end():
    lb.see(tk.END)


def see_top():
    lb.see(0)


def show():
    # global lb
    with open(myfile, "r", encoding='utf8') as f:
        L = f.readlines()
        for line in L:
            line = line.strip("\n")
            print(line)
            lb.insert('end', line)


def add(event=None):
    with open(myfile, "a", encoding='utf8') as fp:
        fp.write(words.get() + "\n")
    lb.delete(0, 'end')
    show()
    see_end()
    words.delete(0, 'end')


def Q():
    ans = tk.messagebox.askyesno(
        title='Quit', message='Are you really want to quit??')
    print(ans)
    if ans:
        window.quit()


def clean():
    ans = tk.messagebox.askyesno(
        title='text clean', message='Are you really want to clean the text??')
    if ans:
        lb.delete(0, 'end')
        with open(myfile, "w", encoding='utf8') as fp:
            fp.write("")


words = tk.Entry(window)
words.bind('<Return>', add)
words.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)
tk.Button(window, text="輸入", bg="#B088FF", command=add).place(
    relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1,
)


sb = tk.Scrollbar()
lb = tk.Listbox(yscrollcommand=sb.set,  height=10,
                font=14, fg='mediumblue', bg='#CCEEFF')


show()

lb.place(relwidth=0.97, relheight=0.5,)
sb.place(
    relx=0.97, rely=0, relwidth=0.03, relheight=0.5,)
sb.config(command=lb.yview)

frame1 = tk.Frame(window, )
frame1.place(relx=0.5, rely=0.5)
tk.Button(frame1, text='END', bg="#B088FF",
          command=see_end, width=10).grid(row=0, column=0, ipady=5, pady=5)
tk.Button(frame1, text='TOP', bg="#B088FF",
          command=see_top, width=10).grid(row=1, column=0, ipady=5, pady=5)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='clear text', command=clean)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=Q)
window.config(menu=menubar)

window.mainloop()
