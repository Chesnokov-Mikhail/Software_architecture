from ModelElements import Vector3D

class Angle3D:

    __vectorA: Vector3D
    __vectorB: Vector3D
    __angle: float
    def __init__(self, vectorA: Vector3D, vectorB: Vector3D):
        self.__vectorA = vectorA
        self.__vectorB = vectorB

    def get_angle3D(self) -> tuple[Vector3D, Vector3D]:
        return (self.__vectorA, self.__vectorB)

    def get_angle(self) -> float:
        return self.__angle