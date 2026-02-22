from pathlib import Path
from waffle.matcher import Matcher
from model_start_test import example2_input

def test_solver_example2():
    matcher = Matcher(Path("src/waffle/valid-words.txt"))
    input = example2_input()
    for word in input.words():
        regex = input.word_regex(word)
        matches = matcher.matches(regex)
        print(f"regex: {regex}, matches: {len(matches)}")
        if len(matches) < 6:
            print(f"\tmatches: {matches}")
    assert False