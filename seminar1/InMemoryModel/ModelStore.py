from InMemoryModel import IModelChanger, IModelChangedObserver
from ModelElements import PoligonalModel, Scene, Flash, Camera
class ModelStore (IModelChanger):

    __observers: list([IModelChangedObserver])
    def __init__(self):
        pass

    def notifyChange(self):
        for observer in self.__observers:
            observer

