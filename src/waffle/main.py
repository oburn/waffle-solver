from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Input, Static

WAFFLE_BLOCKED = {(1, 1), (3, 1), (1, 3), (3, 3)}  # corners

class Cell(Input):
    def __init__(self, r: int, c: int) -> None:
        super().__init__(
            value="",
            placeholder="",
            max_length=1,
            restrict=r"[a-z]*",
            id=f"cell-{r}-{c}",
            classes="cell",
        )
        self.r = r
        self.c = c

class Block(Static):
    """A non-playable cell (corner)."""
    def __init__(self, r: int, c: int) -> None:
        super().__init__("", id=f"block-{r}-{c}", classes="block")
        self.r = r
        self.c = c

class WaffleApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #waffle {
        layout: grid;
        grid-size: 5 5;
        grid-gutter: 0 0;
    }

    .cell, .block {
        width: 5;          /* room for borders + centered letter */
        height: 3;
        content-align: center middle;
        border: solid $foreground;
    }

    .cell {
        padding: 0 0;
    }

    .block {
        background: $panel;
        color: $text-muted;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid(id="waffle"):
            for r in range(5):
                for c in range(5):
                    if (r, c) in WAFFLE_BLOCKED:
                        yield Block(r, c)
                    else:
                        yield Cell(r, c)

if __name__ == "__main__":
    WaffleApp().run()