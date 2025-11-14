from aula_novatos.exercice_6 import prime_factor


def test_example() -> None:
    assert 29 == prime_factor(13195)


def test_wanted() -> None:
    assert 6857 == prime_factor(600851475143)
