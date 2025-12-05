from pytest import raises

from aula_novatos.exercice_33 import distance


def test_example():
    assert 7 == distance("CATCGTAATGACGGCCT")


def test_wanted():
    with raises(ValueError, match="Strands must be of equal length."):
        distance("CATCGTAATGACGGCC")
