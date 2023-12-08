from abc import ABC, abstractmethod
from Table import Table

class AbstractBuilderTable:

    """
        добавляем тип создаваемого стола
    """
    @abstractmethod
    def create_type_table(self):
        raise NotImplementedError

    @abstractmethod
    def GetProduct(self) -> Table:
        raise NotImplementedError