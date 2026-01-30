def prime_factor(number: int) -> int:
    """Retorna o maior fator primo de um número.

    Se o número for menor que 2, ele é retornado como está.

    :param number: int - número de entrada.
    :return: int - maior fator primo.
    """
    if number < 2:
        return number

    p = 2
    while p * p <= number:
        if number % p == 0:
            number //= p
        else:
            p += 1

    return number
