from typing import List


class Function:
    _operands: List[str]
    _operations: List[str]

    def __init__(self, operands: List[str], operation: str) -> None:
        self._operands = operands
        self._operation = operation

    @property
    def operands(self):
        return self._operands

    @property
    def operation(self):
        return self._operation
