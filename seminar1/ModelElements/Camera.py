from ModelElements import Point3D, Angle3D

class Camera:

    __location: Point3D
    __angle: Angle3D
    __counter: int = 40
    __id: int

    def __init__(self, location: Point3D, angle: Angle3D):
        self.__angle = angle
        self.__location = location
        self.__id = ++Camera.__counter

    def rotate(self, angle: Angle3D):
        print(f"Rotate Camera id = {self.__id} to {angle}")

    def move(self, point: Point3D):
        print(f"Move Camera id = {self.__id} to {point}")

    def get_id(self):
        return self.__id