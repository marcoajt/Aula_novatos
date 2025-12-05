from aula_novatos.exercice_34 import sum_numbers


def test_example():
    assert 26 == sum_numbers(15)


def test_wanted():
    assert 1_366 == sum_numbers(1_000)
