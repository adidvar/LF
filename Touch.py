import Controller
import Effect


class Touch(Controller.Controller):
    effects: [Effect] = []

    def start(self):
        pass

    def damage(self, value, absolute: bool, sender):
        pass

    # ABSOLUTE чи стагер настіки жосткий що збиває анімації
    # , причому це int тобто це рівень збивання анімації -1,
    # якщо рівень менше блокування анімації в гравця то анімація не скидується інакше скидується
    # 1 - безкінечність
    # рівень скидання
    def stun(self, time, absolute: int, sender):
        pass

    def silence(self, time):
        pass

    def add_effect(self, effect):
        self.effects.append(effect)
        effect.start()

    def tick(self, delta_time):
        for x in self.effects:
            x.update(delta_time)




