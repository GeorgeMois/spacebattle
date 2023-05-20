import os
import pygame as pg

W, H = 900, 500
FPS = int(60)
clock = pg.time.Clock()

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

red_ship_img = pg.image.load(os.path.join(media_folder, 'spaceship_red.png'))
yellow_ship_img = pg.image.load(os.path.join(media_folder, 'spaceship_yellow.png'))
background_img = pg.image.load(os.path.join(media_folder, 'space.png'))
