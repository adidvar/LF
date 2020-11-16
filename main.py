import Render
import pygame
import sys
import HpController
import AnimationController
import PhysicsController
import Touch
import Player
import Controller

r = Render.Render()
env: Controller.Controller= []
env.append(AnimationController.AnimationController(env))
env.append(HpController.HpController(env))
env.append(PhysicsController.PhysicsController(env))
env.append(Touch.Touch(env))

env[0].start()
env[1].start({"hp" : (50, 100)}, lambda x: x)
env[2].start(1.0 , (0.0 , 0.0 , 0.0) , (200,100))
env[3].start()

p = Player.Player(env)

while 1:
    r.display()
    p.tick(10)
    p.render(r)
