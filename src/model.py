from enum import Enum, auto

class CellInputState(Enum):
    EXACT = auto()  # green state - leter is exactly in the right place
    ALONG = auto()  # yellow state - letter used elsewhere in the word
    MISS = auto()  # clear state - letter is not used in the word
    INVALID = auto()  # invalid state - picked a wrong point

class CellInput():
    def __init__(self, char: str, state: CellInputState) -> None:
        self.state = state
        self.char = char
        
type Input = tuple[
    tuple[CellInput, CellInput, CellInput, CellInput, CellInput],
    tuple[CellInput, None, CellInput, None, CellInput],
    tuple[CellInput, CellInput, CellInput, CellInput, CellInput],
    tuple[CellInput, None, CellInput, None, CellInput],
    tuple[CellInput, CellInput, CellInput, CellInput, CellInput],
]

class InitialState:
    def __init__(self, start_state: Input) -> None:
        self.start_state = start_state

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
        