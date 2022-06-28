from interfaces.person.iracer import IRacer
from person import Person


class Racer(IRacer, Person):
    _awards_count: int

    def __init__(self, name: str, awards_count: int):
        super().__init__(name)
        self._awards_count = awards_count

    def get_awards_count(self) -> int:
        return self._awards_count
