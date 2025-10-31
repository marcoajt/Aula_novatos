def problem_1(limit: int) -> int:
    """implementação do exercicio 1 do project euler

    Args:
        limit (int): limite do intervalo

    Returns:
        int: retorno da soma do intervalo
    """
    return sum([item for item in range(limit) if not item % 3 or not item % 5])
