import webbrowser
import tkinter as tk
from tkinter import messagebox
import pickle
from PIL import Image
import tkinter.font as tkFont

window = tk.Tk()
window.title("Welcome to Angelo's Tkinter login")
window.geometry('450x700')

# welcome image
canvas = tk.Canvas(window,  width=500, height=800)
image_file = tk.PhotoImage(file='hello.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
# communicate image
image_file1 = tk.PhotoImage(file='ig.gif')
image1 = canvas.create_image(80, 410, anchor="nw", image=image_file1)

im_temp = Image.open('email.gif')
im_temp = im_temp.resize((60,60), Image.ANTIALIAS)
im_temp.save("email.gif", "gif")
image_file2 = tk.PhotoImage(file='email.gif')
image2 = canvas.create_image(75, 455, anchor="nw", image=image_file2)
tk.Label(window, text='angeloewn@csie.io', font='Arial',fg='#0066FF',
         bg="#AAFFEE").place(x=150, y=465)

im_temp = Image.open('fb.png')
im_temp = im_temp.resize((40, 40), Image.ANTIALIAS)
im_temp.save("fb.png", "png")
image_file3 = tk.PhotoImage(file='fb.png')
image3 = canvas.create_image(85, 500, anchor="nw", image=image_file3)

canvas.pack(side='top')
#link url

def callback(url):
    webbrowser.open_new(url)


link1 = tk.Label(window, text="wen_19990317", fg="#0000CC",
                 cursor="hand2", font=14, bg="#AAFFEE")
link1.place(x=150, y=420)
link1.bind("<Button-1>", lambda e: callback(
    "https://www.instagram.com/wen_19990317/?hl=zh-tw"))

link2 = tk.Label(window, text="Yen Po Wen", fg="#0000CC",
                 cursor="hand2", font=14, bg="#AAFFEE"
                 )
link2.place(x=150, y=510)
link2.bind("<Button-1>", lambda e: callback(
    "https://www.facebook.com/profile.php?id=100007702635147&ref=bookmarks"))


# user information
tk.Label(window, text='Username: ', font='Arial',
         bg="#DDAA00").place(x=90, y=300)
tk.Label(window, text='Password: ', font='Arial',
         bg="#DDAA00").place(x=90, y=340)
tk.Label(window,
 text="By clicking “Sign up”, you agree to our terms of service and privacy statement.").place(x=10, y=590)
tk.Label(window, text='Copyright © 2019 Angelo Inc. All rights reserved', font='Arial',
         bg="#FFCCCC").place(x=10, y=560)

###set the entry
var_usr_name = tk.StringVar()
var_usr_name.set('example@ccu.edu.tw')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name,bg="#FFDDAA")
entry_usr_name.place(x=200, y=303)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(
    window, textvariable=var_usr_pwd, show='*', bg="#FFDDAA")
entry_usr_pwd.place(x=200, y=343)
def mynote(username):
    tk.messagebox.showinfo(
                title='Welcome', message="Let's try our font family change!!")
    window_note = tk.Toplevel(window)
    window_note.geometry('350x200')
    window_note.title('Hello! ' + username)
    familyVar= tk.StringVar()
    def familychange(event):
        f = tkFont.Font(family=familyVar.get())
        print(f)
        text.configure(font=f)

    tup = ("Arial", "Times", "Courier")
    familyVar.set(tup[0])
    family = tk.OptionMenu(window_note, familyVar, *tup, command=familychange)
    family.pack()

    text = tk.Text(window_note)
    text.pack(fill='both', expand=True, padx=3, pady=2)
    text.focus_set()

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)##將結果數據流寫入到文件對像
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(
                title='Welcome', message='How are you? ' + usr_name)
            mynote(usr_name)
        else:
            tk.messagebox.showerror(
                message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                                            'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()
def usr_sign_up():
    def double_check():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror(
                'Error', 'Password and confirm password must be the same!')
            usr_sign_up()
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(
                message='Welcome '+nn+'!! ,Thank you for join our group!')
            window_sign_up.destroy()
    # Toplevel:應用程序中的一個窗口，關閉窗口將銷毀放置在該窗口{1}上的所有子窗口小部件，但不會關閉該程序。
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@ccu.edu.tw')
    tk.Label(window_sign_up, text='Username: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=double_check)
    btn_comfirm_sign_up.place(x=150, y=130)
# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=160, y=375)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=260, y=375)

window.mainloop()