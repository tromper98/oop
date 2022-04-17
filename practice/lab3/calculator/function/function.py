from typing import List


class Function:
    _name: str
    _variables: List[str]
    _operations: List[str]

    def __init__(self, name: str, variables: List[str], operations: List[str]) -> None:
        self._name = name
        self._variables = variables
        self._operations = operations

    @property
    def name(self):
        return self._name

    @property
    def variables(self):
        return self._variables

    @property
    def operations(self):
        return self._operations
