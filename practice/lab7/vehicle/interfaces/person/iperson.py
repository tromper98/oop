from typing import Protocol


class IPerson(Protocol):
    def get_name(self) -> str:
        ...
