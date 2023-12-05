from abc import ABC, abstractmethod

class IModelChangedObserver(ABC):

    @abstractmethod
    def applyUpdateModel(self):
        pass