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
#mixer.music.load("space.ogg")
#mixer.music.set_volume(1)
#mixer.music.play()

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
    def __init__(self):
        super().__init__("doodler_l.png", 266, 410, 77, 78)
        self.left_img = transform.scale(image.load("doodler_l.png"), (77, 78))
        self.right_img = transform.scale(image.load("doodler_r.png"), (77, 78))
        self.jleft_img = transform.scale(image.load("jumper_l.png"), (77, 78))
        self.jright_img = transform.scale(image.load("jumper_r.png"), (77, 78))
        self.speed = 8
        self.jump = False
        self.jumped = False
        self.jump_height = 225
    def jump(self):
        pass
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = self.left_img
        if keys[K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x += self.speed
            self.image = self.right_img


class Platform(GameSprite):
    def __init__(self, x, y):
        super().__init__("platform_1.png", x, u, 102, 27)

    def update(self):   
        if doodler.jumped:
            self.rect.y += jump_height

platforms = sprite.Group()
def generate_platforms():
    pass
bg_image = transform.scale(image.load("background.png"), (WIDTH, HEIGHT))
doodler = Doodler()
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


    display.update()
    clock.tick(FPS)