import pygame
from settings import *
from player import Player
from ray_casting import ray_casting_walls
from drawing import Drawing


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    drawing.background(player.angle)
    drawing.fps(clock)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls)
    player.movement()
    clock.tick(FPS)

