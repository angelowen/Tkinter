
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title('my window')



def at(window):
        def ball_update():
            canvas.move(pic1, 0, 10)
            canvas.move(pic0, 0, 10)
        def move_active():       
            ball_update()
            window.after(200, move_active)

        canvas = tk.Canvas(window,bg='white', height=500, width=800)

        image1 = Image.open("images.png")
        image1 = image1.resize((50, 50), Image.ANTIALIAS)
        newpic1 = ImageTk.PhotoImage(image1)
        pic0=canvas.create_image(60, 60, anchor='nw', image=newpic1)
    
        image = Image.open("images.png")
        image = image.resize((50, 50), Image.ANTIALIAS)
        newpic = ImageTk.PhotoImage(image)
        pic1=canvas.create_image(10, 10, anchor='nw', image=newpic)
        canvas.pack()
        move_active()
        window.mainloop()
        #hello


at(window)
