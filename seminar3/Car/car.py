from abc import ABC, abstractmethod
from Car import Color, CarType, FuelType, GearboxType

class Car(ABC):
    """
    Абстрактный класс автомобиля
    """
    # марка
    __make: str
    # модель
    __model: str
    # цвет
    __color: Color
    # тип авто
    __type: CarType
    # Число колес
    __wheelsCount: int
    # Тип топлива
    __fuelType: FuelType = FuelType.PETROL
    # Тип коробки передач
    __gearboxType: GearboxType = GearboxType.MT
    # Объем двигателя
    __engineCapacity: float
    def __init__(self, make: str, model: str, color: Color, cartype: CarType, engineCapacity: float):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__type = cartype
        self.__engineCapacity = engineCapacity
        self.wheelsCount = 4
        self.fuelType = FuelType.PETROL
        self.gearboxType = GearboxType.MT

    # Число колес
    @property
    def wheelsCount(self) -> int:
        return self.__wheelsCount

    @wheelsCount.setter
    def wheelsCount(self, value: int):
        if value > 0:
            self.__wheelsCount = value
        else:
            raise ValueError("Количество колес 1 и более")

    @property
    def fuelType(self) -> FuelType:
        return self.__fuelType

    @fuelType.setter
    def fuelType(self, value: FuelType):
        self.__fuelType = value

    @property
    def gearboxType(self) -> GearboxType:
        return self.__gearboxType

    @gearboxType.setter
    def gearboxType(self, value: GearboxType):
        self.__gearboxType = value

    # Движение
    @abstractmethod
    def movement(self):
        raise NotImplementedError
    # Обслуживание
    @abstractmethod
    def maintenance(self):
        raise NotImplementedError
    # Переключение передач
    @abstractmethod
    def gearShifting(self) -> bool:
        raise NotImplementedError
    # Включение фар
    @abstractmethod
    def switchHeadlights(self) -> bool:
        raise NotImplementedError

    # Включение дворников
    @abstractmethod
    def switchWipers(self) -> bool:
        raise NotImplementedError
