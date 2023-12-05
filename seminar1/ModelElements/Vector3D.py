from ModelElements import Point3D
class Vector3D:

    __point_start: Point3D
    __point_end: Point3D
    def __init__(self, point_start: Point3D, point_end: Point3D):
        self.__point_start = point_start
        self.__point_end = point_end

    def set_vector3D(self, point_start: Point3D, point_end: Point3D):
        self.__point_start = point_start
        self.__point_end = point_end

    def get_point_start(self) -> Point3D:
        return self.__point_start

    def get_point_end(self) -> Point3D:
        return self.__point_end