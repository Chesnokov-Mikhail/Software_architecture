import enum
from enum import Enum, unique
@unique
class CarType(Enum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    PICKUP = "pickup"
    SPORT = "sport"