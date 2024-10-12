class Human:
    def __init__(self, name, birth):
        self.name = name
        self.barth = birth

    def say_name(self):
        print(self.name)


class Tomer(Human):
    def __init__(self, name, braf, tomerisbad):
        super().__init__(name, braf)
        self.tomerisbad = tomerisbad

    def sup(self):
        super().say_name()



tomer = Tomer('toffrtrtrtrmer', 'bru', 'yes')
tomer.sup()


