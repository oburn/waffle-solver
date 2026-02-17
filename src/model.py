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
        
type Rows = tuple[
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
    input: Rows

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
    def non_exact_inputs(self) -> set[CellInput]:
        non_exact: set[CellInput] = set()
        for word_cells in self.input:
            for cell in word_cells:
                if cell is not None and cell.state != CellInputState.EXACT:
                    non_exact.add(cell)
        return non_exact

    def basic_facts_at(self, cell: CellInput) -> set[FactAt]:
        facts: set[FactAt] = set()

        if cell.state == CellInputState.EXACT:
            facts.add(FactAt(cell.pt, cell.char, Fact.MUST_BE))
            # TODO: need to add not facts for the axis
        elif cell.state == CellInputState.MISS:
            facts.add(FactAt(cell.pt, cell.char, Fact.CANNOT_BE))
            # TODO: need to add CANNOT_BE facts for the axis
            # TODO: need to add COULD_BE facts for all other cells
        else:
            facts.add(FactAt(cell.pt, cell.char, Fact.CANNOT_BE))
            # TODO: need to add COULD_BE facts for all other cells
            # NOTE: should track the fact for the axis that there must by at least one other cell with the same char
        return facts

    def axis_cells_for(self, cell: CellInput) -> set[CellInput]:
        axis_cells: set[CellInput] = set()
        for word_cells in self.input:
            for c in word_cells:
                if c is not None and (c.pt.x == cell.pt.x or c.pt.y == cell.pt.y) and c.pt != cell.pt:
                    axis_cells.add(c)
        return axis_cells