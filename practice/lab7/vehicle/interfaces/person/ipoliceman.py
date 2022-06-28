from iperson import IPerson
from interfaces.base.ipassenger import IPassenger


class IPoliceMan(IPerson, IPassenger):
    def get_department_name(self) -> str:
        ...
