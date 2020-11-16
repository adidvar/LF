import Controller
import typing
import Touch


class HpController(Controller.Controller):

    bars: {str: [int, int]} = {}
    resist: typing.Callable = None

    def start(self, bars: [[str, (int, int)]], resist: typing.Callable):
        self.bars = bars
        self.resist = resist

    def damage(self, value: int , absolute: bool, sender= None):
        self.bars["hp"][0] -= value if absolute else self.resist(value)

    def islive(self) -> bool:
        return self.bars["hp"][0] > 0

    def tick(self, delta_time):
        for name in self.bars:
            if self.bars[name][0] > self.bars[name][1]:
                self.bars[name][0] = self.bars[name][1]
            if self.bars[name][0] < 0:
                self.bars[name][0] = 0








