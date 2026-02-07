from src.model import CellStart, CellStartState, StartState


def example1_start_state() -> StartState:
    """Example 1 of creating a StartState for a Waffle puzzle."""
    return (
        (
            CellStart(CellStartState.EXACT, 'E'),
            CellStart(CellStartState.MISS, 'M'),
            CellStart(CellStartState.MISS, 'I'),
            CellStart(CellStartState.MISS, 'J'),
            CellStart(CellStartState.EXACT, 'E'),
        ),
        (
            CellStart(CellStartState.MISS, 'S'),
            None,
            CellStart(CellStartState.ALONG, 'E'),
            None,
            CellStart(CellStartState.MISS, 'D'),
        ),
        (
            CellStart(CellStartState.ALONG, 'G'),
            CellStart(CellStartState.MISS, 'N'),
            CellStart(CellStartState.EXACT, 'A'),
            CellStart(CellStartState.MISS, 'V'),
            CellStart(CellStartState.ALONG, 'N'),
        ),
        (
            CellStart(CellStartState.ALONG, 'L'),
            None,
            CellStart(CellStartState.MISS, 'C'),
            None,
            CellStart(CellStartState.ALONG, 'E'),
        ),
        (
            CellStart(CellStartState.EXACT, 'E'),
            CellStart(CellStartState.MISS, 'U'),
            CellStart(CellStartState.ALONG, 'T'),
            CellStart(CellStartState.MISS, 'R'),
            CellStart(CellStartState.EXACT, 'T'),
        ),
    )


if __name__ == "__main__":
    state = example_start_state()
    print(state)
