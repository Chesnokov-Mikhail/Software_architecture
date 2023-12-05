from ModelElements import Point3D, Angle3D

class Camera:

    __location: Point3D
    __angle: Angle3D

    def __init__(self, location: Point3D, angle: Angle3D):
        self.__angle = angle
        self.__location = location

    def rotate(self, angle: Angle3D):
        print(f"Rotate Camera {self} to {angle}")

    def move(self, point: Point3D):
        print(f"Move Camera {self} to {point}")