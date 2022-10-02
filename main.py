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


    display.update()
    clock.tick(FPS)