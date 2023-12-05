from InMemoryModel import IModelChanger, IModelChangedObserver
from ModelElements import PoligonalModel, Scene, Flash, Camera
class ModelStore(IModelChanger):

    __observers: list[IModelChangedObserver]
    __models: list[PoligonalModel]
    __scenes: list[Scene]
    __flashes: list[Flash]
    __cameras: list[Camera]
    def registerModelChanger(self, observer: IModelChangedObserver):
        self.__observers.append(observer)

    def removeModelChanger(self, observer: IModelChangedObserver):
        self.__observers.remove(observer)

    def __init__(self, models: list[PoligonalModel], scenes: list[Scene], flashes: list[Flash], cameras: list[Camera]):
        self.__models = models
        self.__scenes = scenes
        self.__cameras = cameras
        self.__flashes = flashes
        self.__observers = []

    def notifyChange(self, event: str):
        for observer in self.__observers:
            observer.applyUpdateModel(event)

    def addModel(self, model: PoligonalModel):
        self.__models.append(model)
        self.notifyChange("append model")

    def removeModel(self, model: PoligonalModel):
        self.__models.remove(model)
        self.notifyChange("remove model")

    def addScene(self, scene: Scene):
        self.__scenes.append(scene)
        self.notifyChange("append scene")

    def removeScene(self, scene: Scene):
        self.__scenes.remove(scene)
        self.notifyChange("remove scene")

    def addCamera(self, camera: Camera):
        self.__cameras.append(camera)
        self.notifyChange("append camera")

    def removeCamera(self, camera: Camera):
        self.__cameras.remove(camera)
        self.notifyChange("remove camera")

    def addFlashe(self, flashe: Flash):
        self.__flashes.append(flashe)
        self.notifyChange("append flashe")

    def removeFlashe(self, flashe: Flash):
        self.__flashes.remove(flashe)
        self.notifyChange("remove flashe")

    def getScena(self, id: int) -> Scene:
        for scene in self.__scenes:
            if scene.get_id() == id:
                return scene
        return None
