from pathlib import Path
import re

class Matcher:
    def __init__(self, path: Path) -> None:
        self.words = path.read_text().splitlines()

    def matches(self, regex: str) -> tuple[str, ...]:
        return tuple(word for word in self.words if re.fullmatch(regex, word))

if __name__ == "__main__":
    matcher = Matcher(Path("src/valid-words.txt"))
    print(f"Loaded {len(matcher.words)} words")