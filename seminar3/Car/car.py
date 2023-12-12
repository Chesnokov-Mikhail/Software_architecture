from abc import ABC, abstractmethod
from Car import Color
class Car:

    def __init__(self, make: str, model: str, color: Color):
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def movement(self):
        raise NotImplementedError