import tkinter as tk
import time
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 500
SIZE = 50
window = tk.Tk()
window.title("BounceBall")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


class Ball:
    def __init__(self, window):
        image = Image.open("images.png")
        image = image.resize((SIZE, SIZE), Image.ANTIALIAS)
        newpic = ImageTk.PhotoImage(image)
        a = canvas.create_image(10, 10, anchor='nw', image=newpic)
        self.shape = a

        self.speedx = 9 
        self.speedy = 9 
        self.active = True
        self.move_active()
        window.mainloop()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)  # 移動的圖形和x,y
        pos = canvas.coords(self.shape)
        # print(pos)
        if pos[0]+SIZE >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[1]+SIZE >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            window.after(40, self.move_active)  # changed from 10ms to 30ms


ball = Ball(window)
