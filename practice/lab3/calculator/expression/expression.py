from typing import List, Optional


class Expression:
    _left_operand: Optional[str]
    _right_operands: List[str]
    _operation: Optional[str]
    _possible_operators: List[str]

    def __init__(self, left_operand: str = None, right_operands: Optional[List[str]] = None, operation: Optional[str] = None):
        self._left_operand = left_operand
        self._right_operands = right_operands
        self._operation = operation

    @property
    def left_operand(self) -> str:
        return self._left_operand

    @property
    def right_operands(self) -> List[str]:
        return self._right_operands

    @property
    def operation(self) -> str:
        return self._operation

    @staticmethod
    def parse_expr(expr: str):
        equal_pos: int = expr.find('=')
        if equal_pos == -1:
            return Expression(expr)

        left_operand: str = expr[:equal_pos].lstrip().rstrip()
        right_expr: str = expr[equal_pos + 1:]
        operator: str = Expression._get_operator_pos(right_expr)
        right_operands: List[str] = [operand.lstrip().rstrip() for operand in right_expr.split(operator)]

        if right_operands[0] == '' and operator == '-':
            negative_number = operator + right_operands[1]
            right_operands = [negative_number]

        return Expression(left_operand, right_operands, operator)

    @staticmethod
    def _get_operators() -> List[str]:
        operators: List[str] = ['+', '-', '*', '/']
        return operators

    @staticmethod
    def _get_operator_pos(expr: str) -> Optional[str]:
        for operator in Expression._get_operators():
            if operator in expr:
                return operator

        return None
