from enum import Enum, auto

class CellStartState(Enum):
    EXACT = auto()  # green state - leter is exactly in the right place
    ALONG = auto()  # yellow state - letter used elsewhere in the word
    MISS = auto()  # clear state - letter is not used in the word
    INVALID = auto()  # invalid state - picked a wrong point

class CellStart():
    def __init__(self, state: CellStartState, char: str) -> None:
        self.state = state
        self.char = char
        
type StartState = tuple[
    tuple[CellStart, CellStart, CellStart, CellStart, CellStart],
    tuple[CellStart, None, CellStart, None, CellStart],
    tuple[CellStart, CellStart, CellStart, CellStart, CellStart],
    tuple[CellStart, None, CellStart, None, CellStart],
    tuple[CellStart, CellStart, CellStart, CellStart, CellStart],
]

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
        