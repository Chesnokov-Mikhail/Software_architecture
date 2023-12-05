from abc import ABC, abstractmethod
from .ModelChangedObserver import IModelChangedObserver

class IModelChanger(ABC):

    @abstractmethod
    def notifyChange(self, event: str):
        raise NotImplementedError

    @abstractmethod
    def registerModelChanger(self, observer: IModelChangedObserver):
        raise NotImplementedError

    @abstractmethod
    def removeModelChanger(self, observer: IModelChangedObserver):
        raise NotImplementedError