class Color:
    __red: int()
    __green: int()
    __blue: int()

    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__blue = blue
        self.__green = green

    def set_red(self, red: int):
        self.__red = red

    def set_green(self, green: int):
        self.__green = green

    def set_blue(self, blue: int):
        self.__blue = blue
