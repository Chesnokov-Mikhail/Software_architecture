from abc import ABC, abstractmethod

class IModelChangedObserver(ABC):

    @abstractmethod
    def applyUpdateModel(self, event: str):
        raise NotImplementedError