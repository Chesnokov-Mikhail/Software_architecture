class Table:
    __TYPE_TABLE = ['кухонный', 'компьютерный', 'журнальный', 'письменный']

    def __init__(self, type_table: str, weight: float, height: float):
        self.__type_table = type_table
        self.__weight = weight
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value <=0:
            raise ValueError('Не может быть меньше или равно 0')
        self.__weight = value

    @weight.deleter
    def weigt(self):
        raise ValueError('Удалить данный атрибут нельзя')

    @property
    def type_table(self):
        return self.__type_table

    @type_table.setter
    def type_table(self, value: str):
        if value in self.__TYPE_TABLE:
            self.__type_table = value
        else:
            raise ValueError('Нет такого типа стола')

    @type_table.deleter
    def type_table(self):
        raise ValueError('Удалить данный атрибут нельзя')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: float):
        if value <=0:
            raise ValueError('Не может быть меньше или равно 0')
        self.__height = value