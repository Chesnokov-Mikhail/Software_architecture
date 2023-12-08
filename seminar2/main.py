import Table
import Director
import BuilderTable

if __name__ == '__main__':
    director = Director.Director()
    builder1 = BuilderTable.ComputerTableBuilder()
    print(director.constructor(builder1))

    builder2 = BuilderTable.KitchenTableBuilder()
    print(director.constructor(builder2))


