import pgzrun
import random

WIDTH = 600
HEIGHT = 600

hp = 0
count = 0
damage = 1
mode = "game"

crit_chance = 0.0
crit_text = None
crit_y = 0
crit_timer = 0

background = Actor("bg")
gallery_button = Actor("bonus", (70, 50))
gallery_button2 = Actor("bonus", (520, 550))
enemy = Actor("enemy_1", (300, 300))

shop_button1 = Actor("bonus", (100, 150))
shop_button2 = Actor("bonus", (300, 150))
shop_button3 = Actor("bonus", (500, 150))

enemy1_gallery = Actor("enemy_1", (100, 100))
enemy2_gallery = Actor("enemy_2", (300, 100))
enemy3_gallery = Actor("enemy_3", (500, 100))

crit_button = Actor("bonus", (100, 550))

music.play("bgm")
music.set_volume(0.8)

def draw():
    if mode == "game":
        background.draw()
        enemy.draw()
        gallery_button.draw()

        screen.draw.text(str(hp), center=(300, 200), color="red", fontsize=30)
        screen.draw.text(str(count), center=(550, 50), fontsize=30)
        screen.draw.text("mağazaya girme", center=(gallery_button.x, gallery_button.y - 5), fontsize=18)

        if crit_text:
            screen.draw.text(
                crit_text,
                center=(enemy.x, crit_y),
                color="yellow",
                fontsize=40
            )

    elif mode == "shop":
        background.draw()

        enemy1_gallery.draw()
        enemy2_gallery.draw()
        enemy3_gallery.draw()

        shop_button1.draw()
        shop_button2.draw()
        shop_button3.draw()

        crit_button.draw()
        gallery_button2.draw()

        screen.draw.text("1", center=(shop_button1.x, shop_button1.y - 5), fontsize=20)
        screen.draw.text("100", center=(shop_button2.x, shop_button2.y - 5), fontsize=20)
        screen.draw.text("1000", center=(shop_button3.x, shop_button3.y - 5), fontsize=20)

        screen.draw.text("10", center=(crit_button.x, crit_button.y +20 ), fontsize=20)
        screen.draw.text("KRİTİK %10", center=(crit_button.x, crit_button.y -5), fontsize=18)

        screen.draw.text("geri dön", center=(gallery_button2.x, gallery_button2.y - 5), fontsize=20)
        screen.draw.text(str(count), center=(550, 50), fontsize=30)

def update():
    global crit_y, crit_timer, crit_text

    if crit_timer > 0:
        crit_y -= 1
        crit_timer -= 1
    else:
        crit_text = None

def on_mouse_down(button, pos):
    global count, hp, mode, crit_chance, crit_text, crit_y, crit_timer

    if button == mouse.LEFT:

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
                music.set_volume(0.6)
                mode = "shop"

        elif mode == "shop":
            if gallery_button2.collidepoint(pos):
                music.play("bgm")
                music.set_volume(0.8)
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

pgzrun.go()





