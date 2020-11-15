class Effect:
    touch = None

    def __init__(self , touch):
        self.subject_env = touch

    def start(self):
        pass

    def tick(self, delta):
        pass
