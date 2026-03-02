from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.events import Click
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
    CSS_PATH = "waffle.tcss"

    def compose(self) -> ComposeResult:
        self.log("Composing the waffle grid...")
        with Grid(id="waffle"):
            for r in range(5):
                for c in range(5):
                    if (r, c) in WAFFLE_BLOCKED:
                        yield Block(r, c)
                    else:
                        c = Cell(r, c)
                        c.classes = "cell exact"
                        c.disabled = True
                        yield c

    @on(Click)  # Center cell only
    def center_clicked(self, event: Click) -> None:
        self.bell()


if __name__ == "__main__":
    WaffleApp().run()