from itertools import combinations as it_combinations


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    """Return all valid digit combinations for a Killer Sudoku cage.

    Args:
        target (int): Sum that the digits in the cage must add up to.
        size (int): Number of cells (digits) in the cage.
        exclude (list[int]): Digits that cannot be used in the cage.

    Returns:
        list[list[int]]: Sorted list of valid combinations.
    """
    digits = [d for d in range(1, 10) if d not in exclude and d <= target]
    result = []

    for comb in it_combinations(digits, size):
        if sum(comb) == target:
            result.append(list(comb))

    result.sort()

    return result
