import pytest

from aula_novatos.exercice_47 import can_chain


def _normalized(dominoes):
    """Normaliza cada peça (a,b) como (min,max) e ordena a lista."""
    return sorted(tuple(sorted(d)) for d in dominoes)


def test_empty_input_empty_output():
    input_dominoes = []
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)


def test_singleton_input_singleton_output():
    input_dominoes = [(1, 1)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)
    assert output_chain[0][0] == output_chain[-1][1]


def test_singleton_that_cant_be_chained():
    input_dominoes = [(1, 2)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None


def test_three_elements():
    input_dominoes = [(1, 2), (3, 1), (2, 3)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)

    for i in range(len(output_chain) - 1):
        assert output_chain[i][1] == output_chain[i + 1][0]

    assert output_chain[0][0] == output_chain[-1][1]


def test_can_reverse_dominoes():
    input_dominoes = [(1, 2), (1, 3), (2, 3)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)

    for i in range(len(output_chain) - 1):
        assert output_chain[i][1] == output_chain[i + 1][0]

    assert output_chain[0][0] == output_chain[-1][1]


def test_cant_be_chained():
    input_dominoes = [(1, 2), (4, 1), (2, 3)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None


def test_disconnected_simple():
    input_dominoes = [(1, 1), (2, 2)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None


def test_disconnected_double_loop():
    input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None


def test_disconnected_single_isolated():
    input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None


def test_need_backtrack():
    input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)

    for i in range(len(output_chain) - 1):
        assert output_chain[i][1] == output_chain[i + 1][0]

    assert output_chain[0][0] == output_chain[-1][1]


def test_separate_loops():
    input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)

    for i in range(len(output_chain) - 1):
        assert output_chain[i][1] == output_chain[i + 1][0]

    assert output_chain[0][0] == output_chain[-1][1]


def test_nine_elements():
    input_dominoes = [
        (1, 2),
        (5, 3),
        (3, 1),
        (1, 2),
        (2, 4),
        (1, 6),
        (2, 3),
        (3, 4),
        (5, 6),
    ]
    output_chain = can_chain(input_dominoes)

    assert output_chain is not None
    assert _normalized(output_chain) == _normalized(input_dominoes)

    for i in range(len(output_chain) - 1):
        assert output_chain[i][1] == output_chain[i + 1][0]

    assert output_chain[0][0] == output_chain[-1][1]


def test_separate_three_domino_loops():
    input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
    output_chain = can_chain(input_dominoes)

    assert output_chain is None
