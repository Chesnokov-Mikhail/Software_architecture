from ModelElements import Poligon, Texture

class PoligonalModel:

    __textures: list([Texture])
    __poligons: list([Poligon])
    __counter: int = 20
    __id: int()
    def __init__(self, poligons: list([Poligon]), textures: list([Texture]) = None):
        self.__poligons = poligons
        self.__textures = textures
        self.__id = ++PoligonalModel.__counter

    def get_textures(self) -> list([Texture]):
        return self.__textures

    def get_poligons(self) -> list([Poligon]):
        return self.__poligons

    def get_id(self):
        return self.__id