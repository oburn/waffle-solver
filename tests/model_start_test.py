from src.model import CellInput, CellInputState, Input



def example1_input() -> Input:
    """Example 1 of creating a StartState for a Waffle puzzle."""
    return (
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
    )


def test_example1_input():
    """Test that example1_start_state returns a valid StartState."""
    state = example1_input()
    
    # Verify structure: should be a 5-tuple
    assert len(state) == 5
    
    # Verify row structure
    assert len(state[0]) == 5  # Row 1: all 5 cells
    assert len(state[1]) == 5  # Row 2: 3 cells + 2 Nones
    assert len(state[2]) == 5  # Row 3: all 5 cells
    assert len(state[3]) == 5  # Row 4: 3 cells + 2 Nones
    assert len(state[4]) == 5  # Row 5: all 5 cells
    
    # Verify None positions in cross pattern
    assert state[1][1] is None
    assert state[1][3] is None
    assert state[3][1] is None
    assert state[3][3] is None
    
    # Verify first cell in first row
    first_cell = state[0][0]
    assert isinstance(first_cell, CellInput)
    assert first_cell.char == 'E'
    assert first_cell.state == CellInputState.EXACT
