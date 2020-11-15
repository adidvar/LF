import Controller
import typing
import Touch


class HpController:

    bars: [{str: [int, int]}] = None
    resist: typing.Callable = None

    def start(self, bars: [[str, (int, int)]], resist: typing.Callable):
        self.bars = bars
        self.resist = resist

    def damage(self, value: int , absolute: bool, sender: typing.Optional[Touch] = None):
        self.bars["hp"][0] -= value if absolute else self.resist(value)

    def islive(self) -> bool:
        return self.bars["hp"][0] > 0

    def tick(self, delta_time):
        for [name, bars] in self.bars:
            if bars[0] > bars[1]:
                bars[0] = bars[1]
            if bars[0] < 0:
                bars[0] = 0








