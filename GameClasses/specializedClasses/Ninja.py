from GameClasses.baseClass.Hero import Hero
class Ninja(Hero):
    def __init__(self,name,idade):
        super().__init__(name,idade)

    def atacar(self):
        return f"Ninja {self._name} atacou usando shuriken"