from src.model import CellInput, CellInputState, InitialState, Input, WordDirection



def example1_input() -> InitialState:
    """Example 1 of creating a StartState for a Waffle puzzle."""
    return InitialState((
        (
            CellInput('E', CellInputState.EXACT),
            CellInput('M', CellInputState.MISS),
            CellInput('I', CellInputState.MISS),
            CellInput('J', CellInputState.MISS),
            CellInput('E', CellInputState.EXACT),
        ),
        (
            CellInput('S', CellInputState.MISS),
            None,
            CellInput('E', CellInputState.ALONG),
            None,
            CellInput('D', CellInputState.MISS),
        ),
        (
            CellInput('G', CellInputState.ALONG),
            CellInput('N', CellInputState.MISS),
            CellInput('A', CellInputState.EXACT),
            CellInput('V', CellInputState.MISS),
            CellInput('N', CellInputState.ALONG),
        ),
        (
            CellInput('L', CellInputState.ALONG),
            None,
            CellInput('C', CellInputState.MISS),
            None,
            CellInput('E', CellInputState.ALONG),
        ),
        (
            CellInput('E', CellInputState.EXACT),
            CellInput('U', CellInputState.MISS),
            CellInput('T', CellInputState.ALONG),
            CellInput('R', CellInputState.MISS),
            CellInput('T', CellInputState.EXACT),
        ),
    ))


def test_example1_input():
    """Test that example1_start_state returns a valid StartState."""
    input = example1_input()
    
    # Verify structure: should be a 5-tuple
    assert len(input.input) == 5
    
    # Verify words() returns 6 WordInput objects (3 horizontal + 3 vertical)
    words = input.words()
    assert len(words) == 6
    
    # Verify horizontal words
    assert words[0].start.x == 0 and words[0].start.y == 0
    assert words[0].direction == WordDirection.HORIZONTAL
    assert words[0].word[0].char == 'E' and words[0].word[0].state == CellInputState.EXACT
    assert words[0].word[1].char == 'M' and words[0].word[1].state == CellInputState.MISS
    assert words[0].word[2].char == 'I' and words[0].word[2].state == CellInputState.MISS
    assert words[0].word[3].char == 'J' and words[0].word[3].state == CellInputState.MISS
    assert words[0].word[4].char == 'E' and words[0].word[4].state == CellInputState.EXACT
    
    assert words[1].start.x == 0 and words[1].start.y == 2
    assert words[1].direction == WordDirection.HORIZONTAL
    assert words[1].word[0].char == 'G' and words[1].word[0].state == CellInputState.ALONG
    assert words[1].word[1].char == 'N' and words[1].word[1].state == CellInputState.MISS
    assert words[1].word[2].char == 'A' and words[1].word[2].state == CellInputState.EXACT
    assert words[1].word[3].char == 'V' and words[1].word[3].state == CellInputState.MISS
    assert words[1].word[4].char == 'N' and words[1].word[4].state == CellInputState.ALONG
    
    assert words[2].start.x == 0 and words[2].start.y == 4
    assert words[2].direction == WordDirection.HORIZONTAL
    assert words[2].word[0].char == 'E' and words[2].word[0].state == CellInputState.EXACT
    assert words[2].word[1].char == 'U' and words[2].word[1].state == CellInputState.MISS
    assert words[2].word[2].char == 'T' and words[2].word[2].state == CellInputState.ALONG
    assert words[2].word[3].char == 'R' and words[2].word[3].state == CellInputState.MISS
    assert words[2].word[4].char == 'T' and words[2].word[4].state == CellInputState.EXACT
    
    # Verify vertical words
    assert words[3].start.x == 0 and words[3].start.y == 0
    assert words[3].direction == WordDirection.VERTICAL
    assert words[3].word[0].char == 'E' and words[3].word[0].state == CellInputState.EXACT
    assert words[3].word[1].char == 'S' and words[3].word[1].state == CellInputState.MISS
    assert words[3].word[2].char == 'G' and words[3].word[2].state == CellInputState.ALONG
    assert words[3].word[3].char == 'L' and words[3].word[3].state == CellInputState.ALONG
    assert words[3].word[4].char == 'E' and words[3].word[4].state == CellInputState.EXACT
    
    assert words[4].start.x == 2 and words[4].start.y == 0
    assert words[4].direction == WordDirection.VERTICAL
    assert words[4].word[0].char == 'I' and words[4].word[0].state == CellInputState.MISS
    assert words[4].word[1].char == 'E' and words[4].word[1].state == CellInputState.ALONG
    assert words[4].word[2].char == 'A' and words[4].word[2].state == CellInputState.EXACT
    assert words[4].word[3].char == 'C' and words[4].word[3].state == CellInputState.MISS
    assert words[4].word[4].char == 'T' and words[4].word[4].state == CellInputState.ALONG
    
    assert words[5].start.x == 4 and words[5].start.y == 0
    assert words[5].direction == WordDirection.VERTICAL
    assert words[5].word[0].char == 'E' and words[5].word[0].state == CellInputState.EXACT
    assert words[5].word[1].char == 'D' and words[5].word[1].state == CellInputState.MISS
    assert words[5].word[2].char == 'N' and words[5].word[2].state == CellInputState.ALONG
    assert words[5].word[3].char == 'E' and words[5].word[3].state == CellInputState.ALONG
    assert words[5].word[4].char == 'T' and words[5].word[4].state == CellInputState.EXACT
    