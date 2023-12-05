from ModelElements import Point3D, Angle3D, Color
class Flash:

    __location: Point3D
    __angle: Angle3D
    __color: Color
    __power: float
    __counter: int = 30
    __id: int()

    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.__color = color
        self.__power = power
        self.__angle = angle
        self.__location = location
        self.__id = ++Flash.__counter

    def rotate(self, angle: Angle3D):
        print(f"Rotate Flash id = {self.__id} to {angle}")

    def move(self, point: Point3D):
        print(f"Move Flash id = {self.__id} to {point}")

    def get_id(self) -> int:
        return self.__id