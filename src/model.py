from enum import Enum, auto

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
class CellInputState(Enum):
    EXACT = auto()  # green state - leter is exactly in the right place
    ALONG = auto()  # yellow state - letter used elsewhere in the word
    MISS = auto()  # clear state - letter is not used in the word
    INVALID = auto()  # invalid state - picked a wrong point

class WordDirection(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    
class CellInput():
    def __init__(self, char: str, state: CellInputState) -> None:
        self.state = state
        self.char = char

type WordCells = tuple[CellInput, CellInput, CellInput, CellInput, CellInput]

class WordInput:
    def __init__(self,
                 start: Point,
                 direction: WordDirection,
                 word: tuple[CellInput, CellInput, CellInput, CellInput, CellInput]) -> None:
        self.start = start
        self.word = word
        self.direction = direction
        
type Input = tuple[
    WordCells,
    tuple[CellInput, None, CellInput, None, CellInput],
    WordCells,
    tuple[CellInput, None, CellInput, None, CellInput],
    WordCells,
]

class InitialState:
    def __init__(self, input: Input) -> None:
        self.input = input

    def words(self) -> tuple[WordInput, WordInput, WordInput, WordInput, WordInput, WordInput]:
        return (
            WordInput(Point(0, 0), WordDirection.HORIZONTAL, self.input[0]),
            WordInput(Point(0, 2), WordDirection.HORIZONTAL, self.input[2]),
            WordInput(Point(0, 4), WordDirection.HORIZONTAL, self.input[4]),
            WordInput(Point(0, 0), WordDirection.VERTICAL, (self.input[0][0], self.input[1][0], self.input[2][0], self.input[3][0], self.input[4][0])),
            WordInput(Point(2, 0), WordDirection.VERTICAL, (self.input[0][2], self.input[1][2], self.input[2][2], self.input[3][2], self.input[4][2])),
            WordInput(Point(4, 0), WordDirection.VERTICAL, (self.input[0][4], self.input[1][4], self.input[2][4], self.input[3][4], self.input[4][4])),
        )