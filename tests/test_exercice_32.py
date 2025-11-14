from aula_novatos.exercice_32 import routes_grid


def test_example():
    assert 6 == routes_grid(2)


def test_wanted():
    assert 137846528820 == routes_grid(20)
