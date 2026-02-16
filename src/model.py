from dataclasses import dataclass
from enum import Enum, auto

@dataclass(frozen=True)
class Point:
    x: int
    y: int
        
class CellInputState(Enum):
    EXACT = auto()  # green state - leter is exactly in the right place
    ALONG = auto()  # yellow state - letter used elsewhere in the word
    MISS = auto()  # clear state - letter is not used in the word
    INVALID = auto()  # invalid state - picked a wrong point

class WordDirection(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    
@dataclass(frozen=True)
class CellInput:
    pt: Point
    char: str
    state: CellInputState

type WordCells = tuple[CellInput, CellInput, CellInput, CellInput, CellInput]

@dataclass(frozen=True)
class WordInput:
    direction: WordDirection
    word: tuple[CellInput, CellInput, CellInput, CellInput, CellInput]
        
type Input = tuple[
    WordCells,
    tuple[CellInput, None, CellInput, None, CellInput],
    WordCells,
    tuple[CellInput, None, CellInput, None, CellInput],
    WordCells,
]

class Fact(Enum):
    MUST_BE = auto()
    CANNOT_BE = auto()
    COULD_BE = auto()

@dataclass(frozen=True)
class FactAt:
    point: Point
    char: str
    fact: Fact

@dataclass(frozen=True)
class InitialState:
    input: Input

    def words(self) -> tuple[WordInput, WordInput, WordInput, WordInput, WordInput, WordInput]:
        return (
            WordInput(WordDirection.HORIZONTAL, self.input[0]),
            WordInput(WordDirection.HORIZONTAL, self.input[2]),
            WordInput(WordDirection.HORIZONTAL, self.input[4]),
            WordInput(WordDirection.VERTICAL, (self.input[0][0], self.input[1][0], self.input[2][0], self.input[3][0], self.input[4][0])),
            WordInput(WordDirection.VERTICAL, (self.input[0][2], self.input[1][2], self.input[2][2], self.input[3][2], self.input[4][2])),
            WordInput(WordDirection.VERTICAL, (self.input[0][4], self.input[1][4], self.input[2][4], self.input[3][4], self.input[4][4])),
        )

    # method that returns the CellInput that are not None in the input as well as not being in EXACT state
    def non_exact_inputs(self) -> list[CellInput]:
        non_exact = []
        for word_cells in self.input:
            for cell in word_cells:
                if cell is not None and cell.state != CellInputState.EXACT:
                    non_exact.append(cell)
        return non_exact

    def basic_facts(self, cell: CellInput) -> list[FactAt]:
        facts: list[FactAt] = []
        return facts