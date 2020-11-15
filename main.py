import Render
import pygame
import sys

r = Render.Render()

image = pygame.image.load("test.jpeg")

z, y, x = 300.0, 0.0, 300.0

while 1:
    r.draw_object(image, (z, y, x), (400.0, 300.0))
    r.draw_floor(image, (z, x), (400.0, 300.0))

    r.display()
