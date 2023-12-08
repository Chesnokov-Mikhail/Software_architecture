from abc import ABC, abstractmethod

class AbstractBuilderTable:

    @abstractmethod
    def registerModelChanger(self, observer: IModelChangedObserver):
        raise NotImplementedError