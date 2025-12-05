from aula_novatos.exercice_36 import number_letter_count


def test_example():
    assert 19 == number_letter_count(5)


def test_wanted():
    assert 21_124 == number_letter_count(1_000)
