import tkinter as tk
window = tk.Tk()
#show
var1 = tk.StringVar() #定義一個變量用來接收
l = tk.Label(window, bg='yellow', width=8, textvariable=var1).pack()
def show():
    value = lb.get(lb.curselection())#獲取光標在這個listbox上選定的值
    var1.set(value)                 
B=tk.Button(window,text="get",command=show).pack()
##scrollbar
sb = tk.Scrollbar()
sb.pack(side='right',fill='y')

lb=tk.Listbox(yscrollcommand= sb.set)
for i in range(1000):
        lb.insert('end',i)
lb.pack(side='right')
sb.config(command=lb.yview)
window.mainloop()
