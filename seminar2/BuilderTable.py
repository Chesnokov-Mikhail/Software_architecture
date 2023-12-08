from AbstractBuilderTable import AbstractBuilderTable
from Table import *

"""
Строитель компьютерного стола
"""
class ComputerTableBuilder(AbstractBuilderTable):
    def __init__(self):
        self.table = Table()

    def create_type_table(self):
        self.table.type = 'компьютерный'
        self.table.down_shelf = Table_down_shelf()
        self.table.box = Box()

    def GetProduct(self) -> Table:
        return self.table

"""
Строитель кухонного стола
"""
class KitchenTableBuilder(AbstractBuilderTable):
    def __init__(self):
        self.table = Table()

    def create_type_table(self):
        self.table.type = 'кухонный'

    def GetProduct(self) -> Table:
        return self.table