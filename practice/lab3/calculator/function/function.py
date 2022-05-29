from typing import List, Optional


class Function:
    _operands: List[str]
    _operation: str  #Заменить на operation

    def __init__(self, operands: List[str], operation: Optional[str] = None) -> None:
        self._operands = operands
        self._operation = operation

    @property
    def operands(self):
        return self._operands

    @property
    def operation(self):
        return self._operation
