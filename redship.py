
from setting import *


class RedShip(pg.sprite.Sprite):
    def __init__(self):
        self.image = red_ship_img
        pg.sprite.Sprite.__init__(self)
        self.speed = 0
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.center = 50, H/2

    def update(self):
        self.speed = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speed = -8
        if keystate[pg.K_d]:
            self.speed = 8
        self.rect.x += self.speed

        self.speed = 0
        if keystate[pg.K_w]:
            self.speed = -8
        if keystate[pg.K_s]:
            self.speed = 8
        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > H:
            self.rect.bottom = H

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > W:
            self.rect.right = W