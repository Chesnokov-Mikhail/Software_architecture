class Texture:

    __counter: int = 1000
    __id: int()
    __name: str()

    def __init__(self, name: str):
        self.__name = name
        self.__id = ++Texture.__counter

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id