from interfaces.person.iperson import IPerson


class Person(IPerson):
    _name: str

    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name
