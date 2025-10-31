from aula_novatos.problem_1 import problem_1


def test_example():
    assert 23 == problem_1(10)


def test_wanted():
    assert 233_168 == problem_1(10**3)
