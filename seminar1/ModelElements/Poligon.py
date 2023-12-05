from Point3D import Point3D

class Poligon:

    __points: list([Point3D])

    def __init__(self, points: list([Point3D])):
        self.__points = points

    def get_points(self) -> list([Point3D]):
        return self.__points
