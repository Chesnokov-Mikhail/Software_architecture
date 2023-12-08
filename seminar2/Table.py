class Table:

    def __str__(self) -> str:
        return str(self.__dir__())

    def __init__(self):
        self.__depth = 0.0
        self.__weight = 0.0
        self.__height = 0.0
        self.legs = Table_legs()
        self.top = Table_top()

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value <=0:
            raise ValueError('Не может быть меньше или равно 0')
        self.__weight = value

    @weight.deleter
    def weigt(self) -> float:
        raise ValueError('Удалить данный атрибут нельзя')

    @property
    def depth(self) -> float:
        return self.__depth

    @depth.setter
    def depth(self, value: float):
        if value <= 0:
            raise ValueError('Не может быть меньше или равно 0')
        self.__depth = value

    @depth.deleter
    def depth(self):
        raise ValueError('Удалить данный атрибут нельзя')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: float):
        if value <=0:
            raise ValueError('Не может быть меньше или равно 0')
        self.__height = value

    @height.deleter
    def height(self):
        raise ValueError('Удалить данный атрибут нельзя')

"""
ножки
"""
class Table_legs:
    def __init__(self):
        self.number_legs = 0
        self.material_legs = ""
        self.color = ""
"""
столешница
"""
class Table_top:
    def __init__(self):
        self.thickness_table_top = 0.0
        self.shape_table_top = ""
        self.color = ""
"""
ящики
"""
class Box:
    def __init__(self):
        self.number = 0
        self.type = ""
"""
полка для клавиатуры
"""
class Table_down_shelf:
    def __init__(self):
        self.thickness_table_top = 0.0
        self.shape_table_top = ""


