from Car import Car
from CarType import CarType
from Color import Color
from FuelType import FuelType
from GearboxType import GearboxType


class SportCar(Car):

    def __init__(self, make: str, model: str, color: Color, cartype: CarType, engineCapacity: float,
                 wheelsCount: int, fuelType: FuelType, gearboxType: GearboxType):
        super().__init__(make, model, color, cartype, engineCapacity)
        self.wheelsCount = wheelsCount
        self.fuelType = fuelType
        self.gearboxType = gearboxType
        
    @property
    def wheelsCount(self) -> int:
        return super().wheelsCount

    @property
    def fuelType(self) -> FuelType:
        return super().fuelType

    @property
    def gearboxType(self) -> GearboxType:
        return super().gearboxType

    def movement(self):
        print(f'{self.__class__.__name__} двигается')

    def maintenance(self):
        print(f'{self.__class__.__name__} обслуживание')

    def gearShifting(self) -> bool:
        print(f'{self.__class__.__name__} переключение передач')

    def switchHeadlights(self) -> bool:
        print(f'{self.__class__.__name__} включение фар')

    def switchWipers(self) -> bool:
        print(f'{self.__class__.__name__} включение дворников')





