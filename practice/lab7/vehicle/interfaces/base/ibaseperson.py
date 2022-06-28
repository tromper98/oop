from typing import Protocol


class IBasePerson(Protocol):
    def get_name(self) -> str:
        ...
