from iperson import IPerson
from interfaces.base.ipassenger import IPassenger


class IRacer(IPerson, IPassenger):
    def get_awards_count(self) -> int:
        ...
