from AbstractBuilderTable import AbstractBuilderTable

class Director:

    def __init__(self):
        super()
    def constructor(self, builder: AbstractBuilderTable):
        builder.create_type_table()
        return builder.GetProduct()