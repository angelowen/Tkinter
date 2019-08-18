import random
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title('Rainning Heart')


def start(window):
    def ball_update():
        for i in range(1000):
            canvas.move(globals()["pics%s" % i], 0, 10)

    def move_active():
        ball_update()
        window.after(200, move_active)

    canvas = tk.Canvas(window, bg='white', height=500, width=800)
    canvas.create_text(400, 250, fill="darkblue", font="Times 20 italic bold",
                       text="Happy Day!!")  # Hello! My name is Angelo
    for i in range(1000):
        pos = random.randrange(-1000, 1000, 2)
        pos1 = random.randrange(-1000, 1000, 2)
        globals()["image%s" % i] = Image.open("heart.png")
        globals()["image%s" % i] = globals()["image%s" %
                                             i].resize((50, 50), Image.ANTIALIAS)
        globals()["newpic%s" % i] = ImageTk.PhotoImage(
            globals()["image%s" % i])
        globals()["pics%s" % i] = canvas.create_image(pos,
                                                      pos1, anchor='nw', image=globals()["newpic%s" % i])
    # image = Image.open("images.png")
    # image = image.resize((50, 50), Image.ANTIALIAS)
    # newpic = ImageTk.PhotoImage(image)
    # pic1 = canvas.create_image(10, 10, anchor='nw', image=newpic)

    canvas.pack()
    move_active()
    window.mainloop()


start(window)
# tk.Label(text="哈囉你好嗎?", fg="red", bg="pink").place(relx=0.3, rely=0.3)
