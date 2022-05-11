from typing import List


class Function:
    _variables: List[str]
    _operations: List[str]

    def __init__(self, variables: List[str], operations: List[str]) -> None:
        self._variables = variables
        self._operations = operations

    @property
    def variables(self):
        return self._variables

    @property
    def operations(self):
        return self._operations
