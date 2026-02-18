from model_start_test import example2_input
from waffle.model import Point, Fact

def test_eg2_word1_facts() -> None:
    input = example2_input()
    row1_word = input.words()[0]
    row1_word_facts = input.word_facts(row1_word)
    # print(row1_word_facts)

    facts1 = {f for f in row1_word_facts if f.point == Point(3, 0)}
    print(f"facts1: {facts1}")
    must_be = {f.char for f in facts1 if f.fact == Fact.MUST_BE}
    print(f"must_be: {must_be}")
    could_be = {f.char for f in facts1 if f.fact == Fact.COULD_BE}
    print(f"could_be: {could_be}")
    cannot_be = {f.char for f in facts1 if f.fact == Fact.CANNOT_BE}
    print(f"cannot_be: {cannot_be}")
    refined_could_be = sorted(could_be - cannot_be)
    print(f"refined_could_be: {refined_could_be}")
    refined_could_be_str = f"[{''.join(refined_could_be)}]"

    print(f"refined_could_be_str: {refined_could_be_str.lower()}")

    newby = input.word_regex(row1_word)
    print(f"newby: {newby}")

    last = input.word_regex(input.words()[2])
    print(f"last: {last}")

    assert False