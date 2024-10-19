from GameClasses.baseClass.Hero import Hero
class Guerreiro(Hero):
    def __init__(self,name,idade):
        super().__init__(name,idade)

    def atacar(self):
        return f"Guerreiro {self._name} atacou usando espada"