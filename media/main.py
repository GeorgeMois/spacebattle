from setting import *
from redship import RedShip
from yellowship import YellowShip
from Bullet import Bullet

pg.init()
pg.font.init()

screen = pg.display.set_mode((W, H))
pg.display.set_caption("Space war!")


red_health = 10
yellow_health = 10

all_sprite = pg.sprite.Group()
red_ship = RedShip()
yellow_ship = YellowShip()
all_sprite.add(red_ship)
all_sprite.add(yellow_ship)

bullets_red = pg.sprite.Group()
bullets_yellow = pg.sprite.Group()


def shoot_yellow():
    bullet_y = Bullet(yellow_ship.rect.center, "yellow")
    bullets_yellow.add(bullet_y)
    all_sprite.add(bullets_yellow)


def shoot_red():
    bullet_r = Bullet(red_ship.rect.center, "red")
    bullets_red.add(bullet_r)
    all_sprite.add(bullets_red)


run = True
while run:

    screen.blit(background_img, (0, 0))
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RCTRL:
                shoot_yellow()
            elif event.key == pg.K_LCTRL:
                shoot_red()

    if pg.sprite.spritecollide(red_ship, bullets_yellow, False, pg.sprite.collide_circle):
        run = False

    if pg.sprite.spritecollide(yellow_ship, bullets_red, False, pg.sprite.collide_circle):
        run = False

    all_sprite.update()
    all_sprite.draw(screen)

    pg.display.flip()


pg.quit()
