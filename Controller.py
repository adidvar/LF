class Controller:
    env = []

    # контролери з якими ми співпрацюємо (з яких інформацію беремо)

    def __init__(self, env: []):
        self.env = env

    def tick(self, delta_time: int):
        pass
