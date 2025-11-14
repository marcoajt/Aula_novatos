from aula_novatos.exercice_33 import distance


def test_example():
    assert 7 == distance("CATCGTAATGACGGCCT")


def test_wanted():
    assert ValueError("Strands must be of equal length.") == distance(
        "CATCGTAATGACGGCC"
    )
