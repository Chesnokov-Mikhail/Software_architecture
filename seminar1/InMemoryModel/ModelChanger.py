from abc import ABC, abstractmethod

class IModelChanger(ABC):

    @abstractmethod
    def notifyChange(self):
        pass