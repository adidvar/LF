import Controller
import pygame

class AnimationController(Controller.Controller):
    img = None

    def start(self):
        self.img = pygame.image.load("test.jpeg")

    def tick(self, delta_time):
        pass

    def get_frame(self):
        return self.img

    def get_size(self):
        return (400.0, 300.0)