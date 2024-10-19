from GameClasses.baseClass.Hero import Hero
class Monge(Hero):
    def __init__(self,name,idade):
        super().__init__(name,idade)

    def atacar(self):
        return f"Monge {self._name} atacou usando artes marciais"