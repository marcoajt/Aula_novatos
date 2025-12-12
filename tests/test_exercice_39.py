from aula_novatos.exercice_39 import combinations


def test_1():
    assert combinations(1, 1, []) == [[1]]


def test_2():
    assert combinations(2, 1, []) == [[2]]


def test_3():
    assert combinations(3, 1, []) == [[3]]


def test_4():
    assert combinations(4, 1, []) == [[4]]


def test_5():
    assert combinations(5, 1, []) == [[5]]


def test_6():
    assert combinations(6, 1, []) == [[6]]


def test_7():
    assert combinations(7, 1, []) == [[7]]


def test_8():
    assert combinations(8, 1, []) == [[8]]


def test_9():
    assert combinations(9, 1, []) == [[9]]


def test_cage_with_sum_45_contains_all_digits_1_9():
    assert combinations(45, 9, []) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]


def test_cage_with_only_1_possible_combination():
    assert combinations(7, 3, []) == [[1, 2, 4]]


def test_cage_with_several_combinations():
    assert combinations(10, 2, []) == [[1, 9], [2, 8], [3, 7], [4, 6]]


def test_cage_with_several_combinations_that_is_restricted():
    assert combinations(10, 2, [1, 4]) == [[2, 8], [3, 7]]
