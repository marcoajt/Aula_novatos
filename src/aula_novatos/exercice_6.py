# https://exercism.org/tracks/python/exercises/list-ops
# Operações feito a mão, são funções e como funciona por baixo do pano.


from typing import Any, Callable, Iterable


def append(list1: list, list2: Iterable) -> list:
    list1 += list2
    return list1


def concat(lists: Iterable[Iterable]) -> list:
    return [x for lst in lists for x in lst]


def filter(function: Callable[[Any], bool], list: Iterable) -> list:
    return [x for x in list if function(x)]


def length(list: Iterable) -> int:
    return sum(1 for x in list)


def map(function: Callable[[Any], Any], list: Iterable) -> list:
    return [function(x) for x in list]


def foldl(function: Callable[[Any, Any], Any], list: Iterable, initial: Any) -> Any:
    for x in list:
        initial = function(initial, x)
    return initial


def foldr(function: Callable[[Any, Any], Any], list: Iterable, initial: Any) -> Any:
    for x in list[::-1]:
        initial = function(initial, x)
    return initial


def reverse(list: Iterable) -> list:
    return list[::-1]
