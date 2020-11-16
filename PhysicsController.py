import Controller


class PhysicsController(Controller.Controller):

    mass: float = None
    position: [float, float, float] = None
    size: [float, float] = None
    acceleration: [float, float, float] = [0.0, 0.0, 0.0]
    move_delta: [float, float, float] = [0.0, 0.0, 0.0]

    def start(self, mass: float, start_position: [float, float, float], size: [float, float]):
        self.mass = mass
        self.position = list(start_position)
        self.size = list(size)

    def tick(self, delta_time):
        for x in range(3):
            self.position[x] += self.acceleration[x] * delta_time + self.move_delta[x] * delta_time

        # гравітація + тертя

    def update_size(self, size):
        self.size = size

    def move(self, delta: [float, float, float]):
        for x in range(3):
            self.move_delta[x] += delta[x]

    def add_forge(self, forge: float, vector: [float, float, float]):
        for x in range(3):
            self.acceleration[x] += forge * vector[x] / self.mass

    def get_position(self):
        return self.position
