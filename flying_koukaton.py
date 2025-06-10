import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のsurface
    bg_img2 = pg.image.load("fig/pg_bg.jpg") #背景画像のsurface
    bg_img2 = pg.transform.flip(bg_img2,True,False)#背景画像の反転
    kk_img = pg.image.load("fig/3.png") #こうかとん画像のsurface
    kk_img = pg.transform.flip(kk_img,True,False) #こうかとん画像の反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [tmr, 0])
        screen.blit(bg_img2, [tmr+1600, 0])
        screen.blit(bg_img, [tmr+3200, 0])
        
        key_lst = pg.key.get_pressed()
        
        x=0 #横移動の初期値を設定
        y=0 #縦移動の初期値を設定
        if key_lst: #入力がないとき
            move=(x-1,0) #背景と同じ速度で左に動く
        if key_lst[pg.K_RIGHT]: #右入力があるとき
            x=1 #横移動の初期値を右に進むように設定
            move=(x,y) #右に進む  
        if key_lst[pg.K_LEFT]: #左入力があるとき
            move=(x-2,y) #左に進む
        if key_lst[pg.K_DOWN]: #下入力があるとき
            y=1 #縦移動の初期値を下に進むように設定
            move=(x-1,y) #左下に進む
        if key_lst[pg.K_UP]: #上入力があるとき
            move=(x-1,y-1) #左上に進む
        kk_rct.move_ip(move) #動かす
        
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += -1
        if tmr==-3199:
            tmr=0        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()