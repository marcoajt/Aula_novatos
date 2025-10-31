def problem_1(limit: int) -> int:
    """implementação do exercicio 1 do project euler

    Args:
        limit (int): limite do intervalo

    Returns:
        int: retorno da soma do intervalo
    """
    x = 0
    y = 0

    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            y += x

    return y
