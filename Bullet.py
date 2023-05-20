from setting import *


class Bullet(pg.sprite.Sprite):

    def __init__(self, center, team):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 3))
        self.team = team
        self.image.fill(self.team)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 0

    def update(self):
        if self.team == "yellow":
            self.rect.x -= 5
            if self.rect.x < 0:
                self.kill()

        if self.team == "red":
            self.rect.x += 5
            if self.rect.x > W:
                self.kill()