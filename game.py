import random
import time
from tkinter import *


#下面定義一個球的類，有canvas和color兩個物件
class Ball:  # 定義一個Ball類的函式
    def __init__(self, canvas, paddle, color):  # 這是Ball類的屬性函式，Ball類下的函式都有這些性質
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(
            10, 10, 25, 25, fill=color)  # 返回所繪小球的呼叫值放入物件self.id
        self.canvas.move(self.id, 245, 100)  # 移動小球到（245，100）座標處，
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  # 使得小球左右方向運動隨機
        self.y = -3  # 預設開始的小球向上方運動
        # 畫布高度函式winfo_height()返回值放入canvas_height物件中
        self.canvas_height = self.canvas.winfo_height()
        # winfo_width()返回畫布寬度放入canvas_width物件中
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False  # 設定hit_bottom初始值為false

    def hit_paddle(self, pos):  # 宣告函式，以供呼叫
        # 將球拍的(x1,y1)(x2,y2)的座標放到paddle_pos中
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:  # 比較小球y軸是否在球拍y軸內
                return True  # 表示小球碰到了球拍
        return False  # 表示小球沒有碰到球拍

    def draw(self):  # 宣告draw函式，
        # 移動小球，移動速度為（self.x,self.y），在init中的屬性可以直接用
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)  # 把小球的左上角和右下角的座標以列表形式（可能元組）放入pos物件中
        if pos[1] <= 0:  # 如果小球碰到畫布上方
            self.y = 3  # 則改變移動方向向下方
        if pos[3] >= self.canvas_height:  # 如果小球碰到畫布底端 則返回hit_bottom為True
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:  # 小球碰到了球拍，則改變Y軸方向向上運動
            self.y = -3
        if pos[0] <= 0:  # 如果小球碰到了畫布左邊，則把X軸速度改成每次向右3個畫素
            self.x = 3
        if pos[2] >= self.canvas_width:  # 如果小球碰到了畫布右邊，則把速度改成每次向左3個畫素
            self.x = -3


class Paddle:  # 定義一個paddle類
    def __init__(self, canvas, color):  # paddle類的屬性函式，預設有兩個變數畫布和顏色
        self.canvas = canvas  # 將canvas物件賦給self.canvas
        self.id = canvas.create_rectangle(
            0, 0, 100, 10, fill=color)  # 建立球拍，將球拍的呼叫編號存入self.id
        self.canvas.move(self.id, 200, 300)  # 將球拍移動到（200，300）處
        self.x = 0    #
        self.canvas_width = self.canvas.winfo_width()  # 將畫布的寬度放入canvas_width物件
        # 用bind_all()函式繫結鍵盤左鍵與tun_left函式
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # 繫結鍵盤右鍵與turn_right函式
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):  # 宣告一個draw函式
        self.canvas.move(self.id, self.x, 0)  # 左右移動球拍的速度為self.x，預設不動
        pos = self.canvas.coords(self.id)  # 將球拍的左上角和右下角的座標存入pos物件中
        if pos[0] <= 0:  # 如果球拍x軸小於0，則不再向右移動
            self.x = 0
        elif pos[2] >= self.canvas_width:  # 如果球拍要超過畫布右側了，則球拍的移動速度變為0
            self.x = 0

    def turn_left(self, evt):  # 這裡的evt是呼叫方傳過來的引數，改變球拍的移動速度向左，
        self.x = -5

    def turn_right(self, evt):  # 改變球拍的移動速度向右每次5個畫素
        self.x = 5


#建立框架並且命名和固定，然後建立該框架的畫布
tk = Tk()  # 建立框架物件tk
tk.title('Game')  # 框架物件tk顯示的名字為'game'
tk.resizable(0, 0)  # 固定框架
tk.wm_attributes('-topmost', 1)  # 顯示在最外層
canvas = Canvas(tk, width=500, height=400, bd=0,
                highlightthickness=0)  # 建立畫布canvas，屬於tk框架物件，
canvas.pack()  # 顯示畫布的變化
tk.update()  # 顯示框架的變化


#把類賦值給物件ball，如果呼叫了ball就可以實現該類的作用
paddle = Paddle(canvas, "blue")  # 呼叫拍的類給物件paddle用
ball = Ball(canvas, paddle, 'green')  # 呼叫球的類給物件ball用

while True:  # 要注意while語句以防止死迴圈，先設定為真
    if ball.hit_bottom == False:  # 沒有碰到底部的話執行下面的語句
        ball.draw()  # 呼叫ball物件的函式draw（）
        paddle.draw()  # 呼叫paddle物件的函式draw（）
        tk.update_idletasks()
        tk.update()  # 更新框架
        time.sleep(0.01)  # 睡眠0.01秒
    elif ball.hit_bottom == True:  # 要是小球接觸了底部
        canvas.create_text(200, 100, text='Aha,you lose it,\nHow about try again?', font=(
            'Times', 22))  # 在（200，100）座標處建立文字‘...’，字號22號
        tk.update()  # 更新內容
