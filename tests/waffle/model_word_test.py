from model_start_test import example2_input
from waffle.model import Point

def test_eg2_word1_facts() -> None:
    input = example2_input()
    row1_word = input.words()[0]
    row1_word_facts = input.word_facts(row1_word)
    print(row1_word_facts)

    facts1 = {f for f in row1_word_facts if f.point == Point(0, 0)}
    print(facts1)

    assert row1_word_facts == {}
    assert False