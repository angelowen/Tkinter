import tkinter as tk
cnt=0
window = tk.Tk()
window.title("communication")
window.geometry("200x400")

tk.Text(window).place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)
tk.Button(window, text="輸入", bg="#FF8888").place(
    relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1
)
with open("tmp.txt", "r", encoding='utf8') as f:
    L = f.readlines()
    N=len(L)
    for line in L:
        line = line.strip("\n")
        print(line)
        # tk.Label(window, text="",bg="#DDDDDD").grid(row=cnt, column=0,sticky=tk.E)
        tk.Label(window, text=line,bg="#CCFF99").place(
        relx=1, rely=0+cnt, relheight=0.1, anchor='ne')
        cnt+=0.85/N

window.mainloop()
