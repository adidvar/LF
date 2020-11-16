import Controller
import PhysicsController
import Touch
import AnimationController


class Player:

    controllers = []
    touch: Touch = None
    animation: AnimationController = None
    physics: PhysicsController = None

    def __init__(self, controllers: [Controller]):
        self.controllers = controllers

        for x in controllers:
            if isinstance(x, PhysicsController.PhysicsController):
                self.physics = x
            if isinstance(x , Touch.Touch):
                self.touch = x
            if isinstance(x, AnimationController.AnimationController):
                self.animation = x

    def tick(self, delta_time: int):
        for x in self.controllers:
            x.tick(delta_time)

    def render(self, render):
        render.draw_object(self.animation.get_frame(), self.physics.get_position(), self.animation.get_size())


