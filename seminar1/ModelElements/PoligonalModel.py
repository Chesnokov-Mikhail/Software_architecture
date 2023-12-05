from ModelElements import Poligon, Texture

class PoligonalModel:

    __textures: list([Texture])
    __poligons: list([Poligon])
    def __init__(self, poligons: list([Poligon]), textures: list([Texture])):
        self.__poligons = poligons
        self.__textures = textures

    def get_textures(self) -> list([Texture]):
        return self.__textures

    def get_poligons(self) -> list([Poligon]):
        return self.__poligons