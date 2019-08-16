from tkinter import *
import random
import threading
import time
import os

# 初始雨滴縱坐標
INIT_HEIGHT = 10

# 雨滴創建


def rainmake(canvas, imagefile):
    rainlist = []
    for i in range(10):
        # 根據圖片，創建一排心
        rainlist.append(canvas.create_image(
        100 + 80 * i, INIT_HEIGHT, anchor=NE, image=imagefile))
    return rainlist

# 雨滴下落


def raindown(tk, canvas, imagefile, sec):  # 線程間等待     time.sleep(sec)

    rainlist = rainmake(canvas, imagefile)

    # 每顆心的縱坐標值
    height = [INIT_HEIGHT] * 10
    while True:
         # 每次移動前稍等一會
        time.sleep(0.2)

        # 10顆心一起移動
        for i in range(10):
             # 如果這顆心到底了，則不繼續移動，否則height重置就無效了
            if not height[i] == 0:
                 # 設置下落步調
                rnd = random.randint(5, 50)
                canvas.move(rainlist[i], 0, rnd)
                height[i] = height[i] + rnd
                tk.update()

        for i, h in enumerate(height):
             if h > 600:
                 # 當這顆心走到最下方，則刪除
                canvas.delete(rainlist[i])
                tk.update()
                # 清空這顆心的height 
                height[i] = 0
                print (i,h,height) 
                

        # 10顆心全到底，則跳出循環
        # print(height,height == [0] * 10) 
        if height == [ 0 ] * 10 :
             print ( ' break: ' ,threading.current_thread().name)
             break

def lookloop (tk,canvas,thread) : 
    aliveflg = False
    while True :
         # 5s檢測一次 
        time.sleep(5)
        for th in thread:
            if th.is_alive():     
                aliveflg = True
            else : 
                aliveflg = False 

        if aliveflg == False :
             break # Over 
    canvas.create_text( 200 , 300 ,text= ' 不好意思，雨停了... ' ,fill= ' red ' 
     )
    canvas.pack()
    time.sleep( 5 )
    tk.destroy()

def main () : # 創建窗口對象 
     
    tk = Tk()
    tk.title( ' 七夕之雨' )

    canvas_style = {
         ' bg ' : ' white ' ,
         ' height ' : ' 700 ' ,
         ' width ' : ' 900 ' ,
         ' cursor ' : ' circle '
    }
    # 創建畫布 
    canvas = Canvas(tk,canvas_style)
    canvas.pack()
    # 圖片素材
    if  not os.path.exists( 'images.png ' ):
         raise Exception( 'images.png file does not exists. ' )
    imagefile = PhotoImage(file = "images.png " )

    thread = []
    for i in range( 10 ):
        thread.append(threading.Thread(target =raindown,args= (tk,canvas,imagefile,i)))
    for t in thread:
        t.start()

    # 新開一個線程監控運行中的10個線程 
    threading.Thread(target=lookloop,args= (tk,canvas,thread)).start()

    # 進入消息循環
    tk.mainloop()

if  __name__ == ' __main__ ' :
    main()
