class Timer:
    def __init__(self , time):
        self.time = time
        self.delta = 0

    def set_time(self, time):
        self.time = time

    def update(self , delta_time):
        self.delta += delta_time

    def check(self):
        newdelta = self.delta % self.time
        result = newdelta < self.delta
        self.delta = newdelta
        return result
