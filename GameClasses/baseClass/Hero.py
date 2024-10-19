class Hero:
    def __init__(self, name, idade):
        self._name = name
        self._idade = idade

    @property
    def nome(self):
        return self._name

    @property
    def idade(self):
        return self._idade

    def atacar(self):
        pass