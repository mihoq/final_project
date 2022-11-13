from pygame import *
from random import randint
mixer.init()
font.init()
init()
BLACK = (0, 0, 0)
#створити вікно гри
WIDTH = 532
HEIGHT = 820
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Doodle jump")
clock = time.Clock()
font1 = font.Font("DoodleJump.ttf", 50)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


    def draw(self):
        window.blit(self.image, self.rect)
class Doodler(GameSprite):
    def __init__(self, x, y):
        super().__init__("doodler_l.png", x, y, 77, 78)
        self.rect.x = x
        self.rect.y = y
        # doodler_y = self.rect.y
        self.left_img = transform.scale(image.load("doodler_l.png"), (77, 78))
        self.right_img = transform.scale(image.load("doodler_r.png"), (77, 78))
        self.jleft_img = transform.scale(image.load("jumper_l.png"), (77, 78))
        self.jright_img = transform.scale(image.load("jumper_r.png"), (77, 78))
        self.speed = 15
        self.stand = False
        self.jump = True
        self.k_jump = 0
        self.jumped = False
        self.jump_height = 0
        self.gravity = 1
    # def jump(self):
    #     if self.jump = True:
    #         y_change -= 10
    #         self.jump = False
    
    def update(self):
        collide = sprite.spritecollide(self, platforms, False)
        for k in collide:
            if not self.jump and self.rect.y < k.rect.y:
                self.stand = True
                self.rect.bottom = k.rect.top
                self.jump = True
                self.k_jump = 0
                # if self.image = self.left_img:
                #     self.image = self.jleft_img
                # elif self.image = self.right_img:
                #     self.image = self.jright_img




        if self.k_jump < 20 and self.jump:
            self.rect.y -= self.speed
            self.k_jump += 1
            if self.k_jump == 20:
                self.jump = False
        else:
            self.rect.y += self.speed
            self.k_jump -= 1
            # if self.k_jump == 0:
            #     self.jump = True
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = self.left_img
            if self.rect.x < 1:
                self.rect.x += 450


        if keys[K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x += self.speed
            self.image = self.right_img
            if self.rect.x > 455:
                self.rect.x -= 450



    
class Platform(GameSprite):
    def __init__(self, x, y):
        super().__init__("platform_1.png", x, y, 102, 27)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if doodler.rect.y < 250:
            pass
class Button(GameSprite):
    def __init__(self, x, y):
        super().__init__("play_btn.png", x, y, 200, 75)
        self.rect.x = x
        self.rect.y = y
# doodle_jump = Label(110, 10, 150, 50, None)
# doodle_jump.set_text("Doodle Jump", 40, BLACK)
bg_image = transform.scale(image.load("background.png"), (WIDTH, HEIGHT))
doodler = Doodler(266, 710)
play_btn = Button(170, 400)
platform_1 = Platform(215, 790)
platform_2 = Platform(20, 600)
platform_3 = Platform(420, 600)
platform_4 = Platform(215, 400)
platform_5 = Platform(20, 210)
platform_6 = Platform(420, 210)
platforms = sprite.Group()
platforms.add(platform_1, platform_2, platform_3, platform_4, platform_5, platform_6)
y_change = 0
FPS = 60
run = True
play = False
finish = False

while run and play:
    window.blit(bg_image, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        doodler.update()
        doodler.draw()
        platforms.update()
        platforms.draw(window)
    display.update()
    clock.tick(FPS)
    # doodler_y = update(doodler_y)
#    platforms.draw(window)
while run and not play:
    window.blit(bg_image, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        play_btn.update()
        play_btn.draw()
        if play_btn.collidepoint(x,y):
            play = True
        # doodle_jump.draw
    display.update()
    clock.tick(FPS)