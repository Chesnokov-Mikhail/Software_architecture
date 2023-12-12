from enum import Enum, unique
@unique
class FuelType(Enum):
    DIESEL = "diesel"
    PETROL = "petrol"
    GAS = "gas"
    ELECTRICITY = "electricity"