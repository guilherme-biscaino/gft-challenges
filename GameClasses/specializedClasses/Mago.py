from GameClasses.baseClass.Hero import Hero
class Mago(Hero):
    def __init__(self,name, idade):
        super().__init__(name, idade)

    def atacar(self):
        return f"Mago {self._name} atacou usando magia"
