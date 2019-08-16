import random

import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title('my window')


def at(window):
    def ball_update():
        # pass
        for i in range(1000):
            canvas.move(globals()["pics%s" % i], 0, 10)

    def move_active():
        # pass
        ball_update()
        window.after(200, move_active)

    canvas = tk.Canvas(window, bg='white', height=500, width=800)
    for i in range(1000):
        pos = random.randrange(-1000, 1000, 2)
        pos1=random.randrange(-1000, 1000, 2)
        globals()["image%s" % i] = Image.open("a.png")
        globals()["image%s" % i] = globals()["image%s" %
                                           i].resize((50, 50), Image.ANTIALIAS)
        globals()["newpic%s" % i] = ImageTk.PhotoImage(globals()["image%s" % i])
        globals()["pics%s" % i] = canvas.create_image(pos,
                                                    pos1, anchor='nw', image=globals()["newpic%s" % i])
    # image = Image.open("images.png")
    # image = image.resize((50, 50), Image.ANTIALIAS)
    # newpic = ImageTk.PhotoImage(image)
    # pic1 = canvas.create_image(10, 10, anchor='nw', image=newpic)

    canvas.pack()
    # for j in range(20):
    #     for i in range(10):    
    #             window.after(2000, move_active)
    #             canvas.move(globals()["pics%s" % i], 0, 10)
    move_active()
    window.mainloop()


at(window)
