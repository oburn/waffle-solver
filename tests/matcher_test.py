from pathlib import Path
from src.matcher import Matcher

def test_missing() -> None:
    matcher = Matcher(Path("src/valid-words.txt"))
    assert matcher.matches("^zzzzz$") == ()

def test_exact() -> None:
    matcher = Matcher(Path("src/valid-words.txt"))
    assert matcher.matches("^seria$") == ("seria",)

def test_multiple() -> None:
    matcher = Matcher(Path("src/valid-words.txt"))
    assert matcher.matches("^able[dr]$") == ("abled", "abler")