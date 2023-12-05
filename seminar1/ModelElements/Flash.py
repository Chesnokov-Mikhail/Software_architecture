from ModelElements import Point3D, Angle3D, Color
class Flash:

    __location: Point3D
    __angle: Angle3D
    __color: Color
    __power: float
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.__color = color
        self.__power = power
        self.__angle = angle
        self.__location = location

    def rotate(self, angle: Angle3D):
        print(f"Rotate Flash {self} to {angle}")

    def move(self, point: Point3D):
        print(f"Move Flash {self} to {point}")