from interfaces.base.ipassenger import IPassenger


class IPerson(IPassenger):
    def get_name(self) -> str:
        ...
