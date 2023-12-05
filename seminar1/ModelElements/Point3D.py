class Point3D:

    __x: float()
    __y: float()
    __z: float()

    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z

    def set_x(self, x: float):
        self.__x = x

    def set_x(self, y: float):
        self.__y= y

    def set_z(self, z: float):
        self.__z= z

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_z(self) -> float:
        return self.__z