from interfaces.base.ibasevehicle import IBaseVehicle


class ICar(IBaseVehicle):
    def get_make_of_car(self) -> str:
        ...
