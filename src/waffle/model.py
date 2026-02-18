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
    rows: Rows

    def words(self) -> tuple[WordInput, WordInput, WordInput, WordInput, WordInput, WordInput]:
        return (
            WordInput(WordDirection.HORIZONTAL, self.rows[0]),
            WordInput(WordDirection.HORIZONTAL, self.rows[2]),
            WordInput(WordDirection.HORIZONTAL, self.rows[4]),
            WordInput(WordDirection.VERTICAL, (self.rows[0][0], self.rows[1][0], self.rows[2][0], self.rows[3][0], self.rows[4][0])),
            WordInput(WordDirection.VERTICAL, (self.rows[0][2], self.rows[1][2], self.rows[2][2], self.rows[3][2], self.rows[4][2])),
            WordInput(WordDirection.VERTICAL, (self.rows[0][4], self.rows[1][4], self.rows[2][4], self.rows[3][4], self.rows[4][4])),
        )

    # method that returns the CellInput that are not None in the input as well as not being in EXACT state
    def non_exact_inputs(self) -> set[CellInput]:
        non_exact: set[CellInput] = set()
        for word_cells in self.rows:
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
            for axis_cell in self.axis_cells_for(cell):
                facts.add(FactAt(axis_cell.pt, cell.char, Fact.CANNOT_BE))
            for nei in self.non_exact_inputs():
                if nei.pt not in {f.point for f in facts}:
                    facts.add(FactAt(nei.pt, cell.char, Fact.COULD_BE))
        else:
            facts.add(FactAt(cell.pt, cell.char, Fact.CANNOT_BE))
            for nei in self.non_exact_inputs():
                if nei.pt != cell.pt:
                    facts.add(FactAt(nei.pt, cell.char, Fact.COULD_BE))
            # NOTE: should track the fact for the axis that there must by at least one other cell with the same char
        return facts

    def axis_cells_for(self, cell: CellInput) -> set[CellInput]:
        axis_cells: set[CellInput] = set()
        for word_cells in self.rows:
            for w in word_cells:
                if w is not None and \
                    w.pt != cell.pt and \
                    ((cell.pt.x in {0, 2, 4} and cell.pt.x == w.pt.x) or \
                    (cell.pt.y in {0, 2, 4} and cell.pt.y == w.pt.y)):
                    axis_cells.add(w)
        return axis_cells

    def all_facts(self) -> set[FactAt]:
        facts: set[FactAt] = set()
        for word_cells in self.rows:
            for cell in word_cells:
                if cell is not None:
                    facts.update(self.basic_facts_at(cell))
        return facts

    def word_facts(self, word: WordInput) -> set[FactAt]:
        result: set[FactAt] = set()
        all_facts = self.all_facts()
        for cell in word.word:
            result.update(f for f in all_facts if f.point == cell.pt)
        return result

    def word_regex(self, word: WordInput) -> str:
        regex = "^"
        all_facts = self.all_facts()
        for cell in word.word:
            cell_facts = {f for f in all_facts if f.point == cell.pt}
            must_be = {f.char for f in cell_facts if f.fact == Fact.MUST_BE}
            could_be = {f.char for f in cell_facts if f.fact == Fact.COULD_BE}
            cannot_be = {f.char for f in cell_facts if f.fact == Fact.CANNOT_BE}
            refined_could_be = sorted(could_be - cannot_be)
            if must_be:
                regex += must_be.pop()
            else:
                regex += f"[{''.join(refined_could_be)}]"
        regex += "$"
        return regex
