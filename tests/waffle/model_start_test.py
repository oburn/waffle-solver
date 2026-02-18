from waffle.model import CellInput, CellInputState, Fact, FactAt, InitialState, Point, WordDirection

def example2_input() -> InitialState:
    return InitialState((
        (
            CellInput(Point(0, 0), 'c', CellInputState.EXACT),
            CellInput(Point(1, 0), 'r', CellInputState.EXACT),
            CellInput(Point(2, 0), 'm', CellInputState.MISS),
            CellInput(Point(3, 0), 'v', CellInputState.MISS),
            CellInput(Point(4, 0), 'p', CellInputState.EXACT),
        ),
        (
            CellInput(Point(0, 1), 'e', CellInputState.MISS),
            None,
            CellInput(Point(2, 1), 'r', CellInputState.MISS),
            None,
            CellInput(Point(4, 1), 'g', CellInputState.ALONG),
        ),
        (
            CellInput(Point(0, 2), 'l', CellInputState.ALONG),
            CellInput(Point(1, 2), 'a', CellInputState.MISS),
            CellInput(Point(2, 2), 'i', CellInputState.EXACT),
            CellInput(Point(3, 2), 'v', CellInputState.MISS),
            CellInput(Point(4, 2), 'y', CellInputState.ALONG),
        ),
        (
            CellInput(Point(0, 3), 'e', CellInputState.MISS),
            None,
            CellInput(Point(2, 3), 'n', CellInputState.MISS),
            None,
            CellInput(Point(4, 3), 'b', CellInputState.MISS),
        ),
        (
            CellInput(Point(0, 4), 'e', CellInputState.EXACT),
            CellInput(Point(1, 4), 'l', CellInputState.MISS),
            CellInput(Point(2, 4), 'o', CellInputState.ALONG),
            CellInput(Point(3, 4), 'u', CellInputState.MISS),
            CellInput(Point(4, 4), 'y', CellInputState.EXACT),
        ),
    ))


def example1_input() -> InitialState:
    """Example 1 of creating a StartState for a Waffle puzzle."""
    return InitialState((
        (
            CellInput(Point(0, 0), 'E', CellInputState.EXACT),
            CellInput(Point(1, 0), 'M', CellInputState.MISS),
            CellInput(Point(2, 0), 'I', CellInputState.MISS),
            CellInput(Point(3, 0), 'J', CellInputState.MISS),
            CellInput(Point(4, 0), 'E', CellInputState.EXACT),
        ),
        (
            CellInput(Point(0, 1), 'S', CellInputState.MISS),
            None,
            CellInput(Point(2, 1), 'E', CellInputState.ALONG),
            None,
            CellInput(Point(4, 1), 'D', CellInputState.MISS),
        ),
        (
            CellInput(Point(0, 2), 'G', CellInputState.ALONG),
            CellInput(Point(1, 2), 'N', CellInputState.MISS),
            CellInput(Point(2, 2), 'A', CellInputState.EXACT),
            CellInput(Point(3, 2), 'V', CellInputState.MISS),
            CellInput(Point(4, 2), 'N', CellInputState.ALONG),
        ),
        (
            CellInput(Point(0, 3),'L', CellInputState.ALONG),
            None,
            CellInput(Point(2, 3), 'C', CellInputState.MISS),
            None,
            CellInput(Point(4, 3), 'E', CellInputState.ALONG),
        ),
        (
            CellInput(Point(0, 4), 'E', CellInputState.EXACT),
            CellInput(Point(1, 4), 'U', CellInputState.MISS),
            CellInput(Point(2, 4), 'T', CellInputState.ALONG),
            CellInput(Point(3, 4), 'R', CellInputState.MISS),
            CellInput(Point(4, 4), 'T', CellInputState.EXACT),
        ),
    ))


def test_example1_input():
    """Test that example1_start_state returns a valid StartState."""
    input = example1_input()
    
    # Verify structure: should be a 5-tuple
    assert len(input.rows) == 5
    
    # Verify words() returns 6 WordInput objects (3 horizontal + 3 vertical)
    words = input.words()
    assert len(words) == 6
    
    # Verify horizontal words
    assert words[0].direction == WordDirection.HORIZONTAL
    assert words[0].word[0].pt == Point(0, 0)
    assert words[0].word[0].char == 'E' and words[0].word[0].state == CellInputState.EXACT
    assert words[0].word[1].char == 'M' and words[0].word[1].state == CellInputState.MISS
    assert words[0].word[2].char == 'I' and words[0].word[2].state == CellInputState.MISS
    assert words[0].word[3].char == 'J' and words[0].word[3].state == CellInputState.MISS
    assert words[0].word[4].char == 'E' and words[0].word[4].state == CellInputState.EXACT
    assert words[0].word[4].pt == Point(4, 0)
    
    assert words[1].direction == WordDirection.HORIZONTAL
    assert words[1].word[0].pt == Point(0, 2)
    assert words[1].word[0].char == 'G' and words[1].word[0].state == CellInputState.ALONG
    assert words[1].word[1].char == 'N' and words[1].word[1].state == CellInputState.MISS
    assert words[1].word[2].char == 'A' and words[1].word[2].state == CellInputState.EXACT
    assert words[1].word[3].char == 'V' and words[1].word[3].state == CellInputState.MISS
    assert words[1].word[4].char == 'N' and words[1].word[4].state == CellInputState.ALONG
    
    assert words[2].direction == WordDirection.HORIZONTAL
    assert words[2].word[0].pt == Point(0, 4)
    assert words[2].word[0].char == 'E' and words[2].word[0].state == CellInputState.EXACT
    assert words[2].word[1].char == 'U' and words[2].word[1].state == CellInputState.MISS
    assert words[2].word[2].char == 'T' and words[2].word[2].state == CellInputState.ALONG
    assert words[2].word[3].char == 'R' and words[2].word[3].state == CellInputState.MISS
    assert words[2].word[4].char == 'T' and words[2].word[4].state == CellInputState.EXACT
    
    # Verify vertical words
    assert words[3].direction == WordDirection.VERTICAL
    assert words[3].word[0].pt == Point(0, 0)
    assert words[3].word[0].char == 'E' and words[3].word[0].state == CellInputState.EXACT
    assert words[3].word[1].char == 'S' and words[3].word[1].state == CellInputState.MISS
    assert words[3].word[2].char == 'G' and words[3].word[2].state == CellInputState.ALONG
    assert words[3].word[3].char == 'L' and words[3].word[3].state == CellInputState.ALONG
    assert words[3].word[4].char == 'E' and words[3].word[4].state == CellInputState.EXACT
    assert words[3].word[4].pt == Point(0, 4)
    
    assert words[4].direction == WordDirection.VERTICAL
    assert words[4].word[0].pt == Point(2, 0)
    assert words[4].word[0].char == 'I' and words[4].word[0].state == CellInputState.MISS
    assert words[4].word[1].char == 'E' and words[4].word[1].state == CellInputState.ALONG
    assert words[4].word[2].char == 'A' and words[4].word[2].state == CellInputState.EXACT
    assert words[4].word[3].char == 'C' and words[4].word[3].state == CellInputState.MISS
    assert words[4].word[4].char == 'T' and words[4].word[4].state == CellInputState.ALONG
    
    assert words[5].direction == WordDirection.VERTICAL
    assert words[5].word[0].pt == Point(4, 0)
    assert words[5].word[0].char == 'E' and words[5].word[0].state == CellInputState.EXACT
    assert words[5].word[1].char == 'D' and words[5].word[1].state == CellInputState.MISS
    assert words[5].word[2].char == 'N' and words[5].word[2].state == CellInputState.ALONG
    assert words[5].word[3].char == 'E' and words[5].word[3].state == CellInputState.ALONG
    assert words[5].word[4].char == 'T' and words[5].word[4].state == CellInputState.EXACT
    assert words[5].word[4].pt == Point(4, 4)
    
def test_example1_word1():
    """Test that the first horizontal word in example1_input is correct."""
    input = example1_input()
    word1 = input.words()[1]
    
    print(f"Word 1: {word1}")

    for ci in word1.word:
        if ci.state == CellInputState.MISS:
            print(f"  Char: {ci.char}, State: {ci.state} (should be MISS)")
        elif ci.state == CellInputState.ALONG:
            print(f"  Char: {ci.char}, State: {ci.state} (should be ALONG)")

    for ne in input.non_exact_inputs():
        print(f"Non-exact input: Char: {ne.char}, State: {ne.state}")


def test_example2_exact_cell_facts() -> None:
    input = example2_input()
    facts = input.basic_facts_at(input.rows[0][0])

    assert facts == {FactAt(Point(0, 0), 'c', Fact.MUST_BE)}


def test_example2_miss_cell_facts1() -> None:
    input = example2_input()
    facts = input.basic_facts_at(input.rows[0][3])
    assert facts == {
        # Axis cells
        FactAt(Point(0, 0), 'v', Fact.CANNOT_BE),
        FactAt(Point(1, 0), 'v', Fact.CANNOT_BE),
        FactAt(Point(2, 0), 'v', Fact.CANNOT_BE),
        FactAt(Point(3, 0), 'v', Fact.CANNOT_BE),
        FactAt(Point(4, 0), 'v', Fact.CANNOT_BE),
        # Second row
        FactAt(Point(0, 1), 'v', Fact.COULD_BE),
        FactAt(Point(2, 1), 'v', Fact.COULD_BE),
        FactAt(Point(4, 1), 'v', Fact.COULD_BE),
        # Third row
        FactAt(Point(0, 2), 'v', Fact.COULD_BE),
        FactAt(Point(1, 2), 'v', Fact.COULD_BE),
        FactAt(Point(3, 2), 'v', Fact.COULD_BE),
        FactAt(Point(4, 2), 'v', Fact.COULD_BE),
        # Fourth row
        FactAt(Point(0, 3), 'v', Fact.COULD_BE),
        FactAt(Point(2, 3), 'v', Fact.COULD_BE),
        FactAt(Point(4, 3), 'v', Fact.COULD_BE),
        # Fifth row
        FactAt(Point(1, 4), 'v', Fact.COULD_BE),
        FactAt(Point(2, 4), 'v', Fact.COULD_BE),
        FactAt(Point(3, 4), 'v', Fact.COULD_BE),
    }


def test_example2_miss_cell_facts2() -> None:
    input = example2_input()
    facts = input.basic_facts_at(input.rows[0][2])
    assert facts == {
        # Axis cells
        FactAt(Point(0, 0), 'm', Fact.CANNOT_BE),
        FactAt(Point(1, 0), 'm', Fact.CANNOT_BE),
        FactAt(Point(2, 0), 'm', Fact.CANNOT_BE),
        FactAt(Point(3, 0), 'm', Fact.CANNOT_BE),
        FactAt(Point(4, 0), 'm', Fact.CANNOT_BE),
        FactAt(Point(2, 1), 'm', Fact.CANNOT_BE),
        FactAt(Point(2, 2), 'm', Fact.CANNOT_BE),
        FactAt(Point(2, 3), 'm', Fact.CANNOT_BE),
        FactAt(Point(2, 4), 'm', Fact.CANNOT_BE),
        # Second row
        FactAt(Point(0, 1), 'm', Fact.COULD_BE),
        FactAt(Point(4, 1), 'm', Fact.COULD_BE),
        # Third row
        FactAt(Point(0, 2), 'm', Fact.COULD_BE),
        FactAt(Point(1, 2), 'm', Fact.COULD_BE),
        FactAt(Point(3, 2), 'm', Fact.COULD_BE),
        FactAt(Point(4, 2), 'm', Fact.COULD_BE),
        # Fourth row
        FactAt(Point(0, 3), 'm', Fact.COULD_BE),
        FactAt(Point(4, 3), 'm', Fact.COULD_BE),
        # Fifth row
        FactAt(Point(1, 4), 'm', Fact.COULD_BE),
        FactAt(Point(3, 4), 'm', Fact.COULD_BE),
    }

def test_example2_along_cell_facts() -> None:
    input = example2_input()
    facts = input.basic_facts_at(input.rows[1][4])
    assert facts == {
        # Right column
        FactAt(Point(4, 1), 'g', Fact.CANNOT_BE),
        FactAt(Point(4, 2), 'g', Fact.COULD_BE),
        FactAt(Point(4, 3), 'g', Fact.COULD_BE),
        # First row
        FactAt(Point(2, 0), 'g', Fact.COULD_BE),
        FactAt(Point(3, 0), 'g', Fact.COULD_BE),
        # Second row
        FactAt(Point(0, 1), 'g', Fact.COULD_BE),
        FactAt(Point(2, 1), 'g', Fact.COULD_BE),
        # Third row
        FactAt(Point(0, 2), 'g', Fact.COULD_BE),
        FactAt(Point(1, 2), 'g', Fact.COULD_BE),
        FactAt(Point(3, 2), 'g', Fact.COULD_BE),
        FactAt(Point(4, 2), 'g', Fact.COULD_BE),
        # Fourth row
        FactAt(Point(0, 3), 'g', Fact.COULD_BE),
        FactAt(Point(2, 3), 'g', Fact.COULD_BE),
        FactAt(Point(4, 3), 'g', Fact.COULD_BE),
        # Fifth row
        FactAt(Point(1, 4), 'g', Fact.COULD_BE),
        FactAt(Point(2, 4), 'g', Fact.COULD_BE),
        FactAt(Point(3, 4), 'g', Fact.COULD_BE),
    }


def test_example2_axis_cells_corner() -> None:
    input = example2_input()
    cells = input.axis_cells_for(input.rows[0][0])
    assert cells == {
        input.rows[0][1], input.rows[0][2], input.rows[0][3], input.rows[0][4],
        input.rows[1][0], input.rows[2][0], input.rows[3][0], input.rows[4][0],
    }


def test_example2_axis_cells_offset_middle_horizontal() -> None:
    input = example2_input()
    cells = input.axis_cells_for(input.rows[2][1])

    assert cells == {
        input.rows[2][0], input.rows[2][2], input.rows[2][3], input.rows[2][4],
    }


def test_example2_axis_cells_offset_middle_vertical() -> None:
    input = example2_input()
    cells = input.axis_cells_for(input.rows[1][2])

    assert cells == {
        input.rows[0][2], input.rows[2][2], input.rows[3][2], input.rows[4][2],
    }


def test_example2_axis_cells_middle() -> None:
    input = example2_input()
    cells = input.axis_cells_for(input.rows[2][2])

    assert cells == {
        input.rows[2][0], input.rows[2][1], input.rows[2][3], input.rows[2][4],
        input.rows[0][2], input.rows[1][2], input.rows[3][2], input.rows[4][2],
    }
