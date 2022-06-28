from interfaces.person.ipoliceman import IPoliceMan
from person import Person


class PoliceMan(IPoliceMan, Person):
    _department_name: str

    def __init__(self, name: str, department_name: str):
        super().__init__(name)
        self._department_name = department_name

    def get_department_name(self) -> str:
        return self._department_name
