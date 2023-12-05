from InMemoryModel import IModelChangedObserver

class Observer(IModelChangedObserver):

    name: str
    def __init__(self, name: str):
        self.name = name
    def applyUpdateModel(self, event: str):
        print(f"{self.name} реагирует на изменения {event}")
