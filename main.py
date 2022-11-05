from pygame import *
from random import randint
mixer.init()
font.init()
init()
#створити вікно гри
WIDTH = 532
HEIGHT = 820
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Doodle jump")
clock = time.Clock()
font1 = font.SysFont("Impact", 50)


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
        self.speed = 8
        self.jump = False
        self.jumped = False
        self.jump_height = 0
        self.gravity = 1
    def jump(self):
        if self.jump = True:
            y_change -= 10
            self.jump = False
    
    def update(self):
        self jump
        global y_change
        self.jump_height = 10
        self.gravity = 1
        if jump:

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

    # def update(self):   
    #     if doodler.jumped:
    #         self.rect.y += jump_height

# class Wall(sprite.Sprite):
#     def __init__(self, x, y, width, height, color = (255, 113, 31)):
#         super().__init__()
#         self.img = Surface((width, height))
#         self.rect = self.img.get_rect()
#         self.img.fill(color)
        # self.rect.x = x
        # self.rect.y = y
#         self.width = width
#         self.height = height

bg_image = transform.scale(image.load("background.png"), (WIDTH, HEIGHT))
doodler = Doodler(266, 410)
platform_1 = Platform(215, 790)
y_change = 0
FPS = 60
run = True
finish = False
while run:
    window.blit(bg_image, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        doodler.update()
        doodler.draw()
        platform_1.update()
        platform_1.draw()
    # doodler_y = update(doodler_y)
#    platforms.draw(window)
    display.update()
    clock.tick(FPS)