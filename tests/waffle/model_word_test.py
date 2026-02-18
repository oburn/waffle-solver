from model_start_test import example2_input

def test_eg2_word_regex() -> None:
    input = example2_input()

    assert input.word_regex(input.words()[0]) == "^cr[abeglouy][abeglnoruy]p$"
    assert input.word_regex(input.words()[1]) == "^[bgmnoruy][beglmnoruy]i[beglmnoruy][eglmnoru]$"
    assert input.word_regex(input.words()[2]) == "^e[abegmnorvy][abegvy][abegmnorvy]y$"
    assert input.word_regex(input.words()[5]) == "^p[aelmnoruvy][eglmnoru][aeglmnoruvy]y$"