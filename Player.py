import Controller


class Player:

    controllers = []
    Touch = None

    def __init__(self, controllers: [Controller]):
        self.controllers = controllers

    def tick(self, delta_time : int):
        for x in self.controllers:
            x.tick(delta_time)

    def render(self):
        pass

