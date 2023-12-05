from ModelElements import PoligonalModel, Flash, Camera

class Scene:

    __counter: int = 10
    __models: list([PoligonalModel])
    __flashes: list([Flash])
    __cameras: list([Camera])
    __id: int()
    def __init__(self, models: list([PoligonalModel]), flashes: list([Flash]), cameras: list([Camera])):
        self.__cameras = cameras
        self.__flashes = flashes
        self.__models = models
        self.__id = ++Scene.__counter

    def get_id(self):
        return self.__id

    def get_models(self) -> list([PoligonalModel]):
        return self.__models

    def get_flashes(self) -> list([Flash]):
        return self.__flashes

    def get_cameras(self) -> list([Camera]):
        return self.__cameras
    
    def metod1(self) -> bool:
        print(f"Runing Metod1 Scene id = {self.__id}")
        return True

    def metod2(self) -> bool:
        print(f"Runing Metod2 Scene id = {self.__id}")
        return True


