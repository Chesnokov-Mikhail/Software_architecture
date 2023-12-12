from abc import ABC, abstractmethod
from Car import Color, CarType, FuelType, GearboxType

# /**
#  * 1. Спроектировать абстрактный класс «Car» у которого должны
#  * быть свойства: марка, модель, цвет, тип кузова, число колёс, тип
#  * топлива, тип коробки передач, объём двигателя; методы:
#  * движение, обслуживание, переключение передач, включение
#  * фар, включение дворников.
#  *
#  * 2. Создать конкретный автомобиль путём наследования класса
#  * «Car».
#  *
#  * 3. Расширить абстрактный класс «Car», добавить метод: подметать
#  * улицу. Создать конкретный автомобиль путём наследования
#  * класса «Car». Провести проверку принципа SRP.
#  *
#  * 4. Расширить абстрактный класс «Car», добавить метод:
#  * включение противотуманных фар, перевозка груза. Провести
#  * проверку принципа OCP.
#  *
#  * 5. Создать конкретный автомобиль путём наследования класса
#  * «Car», определить число колёс = 3. Провести проверку принципа LSP.
#  *
#  * 6. Создать интерфейс «Заправочная станция», создать метод:
#  * заправка топливом.
#  *
#  * 7. Имплементировать метод интерфейса «Заправочная станция» в
#  * конкретный класс «Car».
#  *
#  * 8. Добавить в интерфейс «Заправочная станция» методы: протирка
#  * лобового стекла, протирка фар, протирка зеркал.
#  *
#  * 9. Имплементировать все методы интерфейса «Заправочная
#  *      * станция» в конкретный класс «Car». Провести проверку
#  *      * принципа ISP. Создать дополнительный/е интерфейсы и
#  *      * имплементировать их в конкретный класс «Car». Провести
#  *      * проверку принципа ISP.
#  *
#  * 10. Создать путём наследования класса «Car» два
#  *      * автомобиля: с бензиновым и дизельным двигателями,
#  *      * имплементировать метод «Заправка топливом» интерфейса
#  *      * «Заправочная станция». Реализовать заправку каждого
#  *      * автомобиля подходящим топливом. Провести проверку принципа DIP.
#  *
#  ** TODO: Домашнее задание:
#  *      * Доработать приложение, спроектированное на семинаре. Добавить тип, описывающий "автомойку" и "сервисную станцию".
#  *      * Продемонстрировать работу получившейся программы,
#  *      * создать несколько типов автомобилей,
#  *      * загнать каждый автомобиль на заправку, а затем и на автомойку.
#  */

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

    @abstractmethod
    def movement(self):
        raise NotImplementedError

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