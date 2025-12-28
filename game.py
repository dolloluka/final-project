import pgzrun
import random

WIDTH = 600
HEIGHT = 600

hp = 0
count = 0
damage = 1
mode = "menu"

crit_chance = 0.0
crit_text = None
crit_y = 0
crit_timer = 0
play_button = Actor("bonus",(300,300))
background = Actor("bg")
background2=Actor("bg2")
gallery_button = Actor("bonus", (70, 50))
gallery_button2 = Actor("bonus", (520, 550))
enemy = Actor("enemy_1", (300, 300))
menu_button= Actor("bonus",(380,550))
shop_button1 = Actor("bonus", (100, 150))
shop_button2 = Actor("bonus", (300, 150))
shop_button3 = Actor("bonus", (500, 150))
shop_button4 = Actor("bonus", (100, 400))
shop_button5 = Actor("bonus", (300, 400))
shop_button6=Actor("bonus",(500,400))
menu_button2=Actor("bonus",(500,550))
enemy1_gallery = Actor("enemy_1", (100, 100))
enemy2_gallery = Actor("enemy_2", (300, 100))
enemy3_gallery = Actor("enemy_3", (500, 100))
enemy4_gallery = Actor("enemy_4",(100,300))
enemy5_gallery = Actor("enemy_5",(300,300))
enemy6_gallery = Actor("enemy_6",(300,300))
enemy7_gallery=Actor("enemy_7",(500,300))
crit_button = Actor("bonus", (100, 550))
boss_spawned = False

music.play("menu")
music.set_volume(0.1)

def draw():
    if mode =="menu":
        menu_button.draw()
        background2.draw()
        play_button.draw()
        screen.draw.text("Oyun Başla", center=(play_button.x ,play_button.y - 5),fontsize=20)
    
    
        
    if mode == "game":
        background.draw()
        enemy.draw()
        gallery_button.draw()
        menu_button2.draw()

        screen.draw.text(str(hp), center=(325, 130), color="red", fontsize=30)
        screen.draw.text(str(count), center=(550, 50), fontsize=30)
        screen.draw.text("Mağazaya girme", center=(gallery_button.x, gallery_button.y - 5), fontsize=18)
        screen.draw.text("Bilgilendirme",center=(menu_button2.x,menu_button2.y -5),fontsize=20)
    if mode=="menu2":
        background2.draw()
        screen.draw.text("BU SADECE BİR TIKLAMA OYUNUDUR",center=(300,100),color="white" ,fontsize=30)
        screen.draw.text("BURADAN ÇIKAMAZSIN",center=(300,200),color="white" ,fontsize=30)
        screen.draw.text("BURDAN ÇIKMAK İSTİYORSAN OYUNU KAPATMALISIN!",center=(300,300),color="white" ,fontsize=30)
        screen.draw.text("BU OYUNUN GİZLİ BİR SONU VARDIR GÖRMEK İSTİYORSANIZ 100000 PUAN YAPMALISINIZ!",center=(300,400),color="white",fontsize=20)
        if crit_text:
            screen.draw.text(crit_text,center=(enemy.x, crit_y),color="yellow",fontsize=40)

    elif mode == "shop":
        background.draw()

        enemy1_gallery.draw()
        enemy2_gallery.draw()
        enemy3_gallery.draw()
        enemy4_gallery.draw()
        enemy5_gallery.draw()
        enemy7_gallery.draw()
        shop_button1.draw()
        shop_button2.draw()
        shop_button3.draw()
        shop_button4.draw()
        shop_button5.draw()
        shop_button6.draw()
        menu_button.draw()
        crit_button.draw()
        gallery_button2.draw()

        screen.draw.text("1", center=(shop_button1.x, shop_button1.y - 5), fontsize=20)
        screen.draw.text("100", center=(shop_button2.x, shop_button2.y - 5), fontsize=20)
        screen.draw.text("1000", center=(shop_button3.x, shop_button3.y - 5), fontsize=20)
        screen.draw.text("1000", center=(shop_button4.x, shop_button4.y - 5), fontsize=20)
        screen.draw.text("1000", center=(shop_button5.x, shop_button5.y - 5), fontsize=20)
        screen.draw.text("10000", center=(shop_button6.x, shop_button6.y - 5), fontsize=20)
        screen.draw.text("10", center=(crit_button.x, crit_button.y +20 ), fontsize=20)
        screen.draw.text("KRİTİK %10", center=(crit_button.x, crit_button.y -5), fontsize=18)

        screen.draw.text("geri dön", center=(gallery_button2.x, gallery_button2.y - 5), fontsize=20)
        screen.draw.text(str(count), center=(550, 50), fontsize=30)
        screen.draw.text("Menüye geri dön",center=(menu_button.x,menu_button.y -5 ),fontsize=20)
def update():
    global crit_y, crit_timer, crit_text,hp,boss_spawned

    if crit_timer > 0:
        crit_y -= 1
        crit_timer -= 1
    else:
        crit_text = None

    if count >= 100000 and not boss_spawned:
        boss_spawned = True
        enemy.image = "enemy_6"
        hp = 0
        music.stop()
        music.play("fallen")
        music.set_volume(1.0)

 
def on_mouse_down(button, pos):
    global count, hp, mode, crit_chance, crit_text, crit_y, crit_timer

    if button == mouse.LEFT:
        if mode =="menu":
            if play_button.collidepoint(pos):
                mode="game"
        if mode == "game":

            if enemy.collidepoint(pos):
                count += 1

                if random.random() < crit_chance:
                    hp += damage * 2
                    crit_text = "CRITICAL!"
                    crit_y = enemy.y - 40
                    crit_timer = 30
                else:
                    hp += damage

                enemy.y = 200
                animate(enemy, tween="bounce_end", duration=0.5, y=230)
                

            elif gallery_button.collidepoint(pos):
                music.play("shop")
                music.set_volume(0.1)
                mode = "shop"
            elif menu_button2.collidepoint(pos):
                mode="menu2"


        elif mode == "shop":
            if gallery_button2.collidepoint(pos):
                music.play("bgm")
                music.set_volume(0.1)
                mode = "game"

            elif crit_button.collidepoint(pos) and count >= 10 and crit_chance == 0:
                count -= 10
                crit_chance = 0.10

            elif enemy1_gallery.collidepoint(pos) and count >= 1:
                count -= 1
                enemy.image = "enemy_1"
                hp = 0

            elif enemy2_gallery.collidepoint(pos) and count >= 100:
                count -= 100
                enemy.image = "enemy_2"
                hp = 0

            elif enemy3_gallery.collidepoint(pos) and count >= 1000:
                count -= 1000
                enemy.image = "enemy_3"
                hp = 0
            
            elif enemy4_gallery.collidepoint(pos) and count >= 1000:
                count -= 1000
                enemy.image = "enemy_4"
                hp = 0

            elif enemy5_gallery.collidepoint(pos) and count >= 1000:
                count -= 1000
                enemy.image = "enemy_5"
                hp = 0
            elif enemy7_gallery.collidepoint(pos) and count >= 10000:
                count -= 10000
                enemy.image = "enemy_7"
                hp = 0
            elif menu_button.collidepoint(pos):
                mode="menu"
                

            
                

pgzrun.go()





