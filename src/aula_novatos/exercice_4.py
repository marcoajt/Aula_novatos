# https://exercism.org/tracks/python/exercises/rotational-cipher

CHARS = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Aplica uma cifra de rotação nas letras de um texto.

    As letras minúsculas e maiúsculas são deslocadas pelo valor de `key`
    dentro do alfabeto; outros caracteres são mantidos.

    :param text: str - texto de entrada.
    :param key: int - número de posições para rotacionar no alfabeto.
    :return: str - texto cifrado com rotação.
    """
    newchars = CHARS[key:] + CHARS[:key]
    trans = str.maketrans(
        CHARS + CHARS.upper(),
        newchars + newchars.upper(),
    )
    return text.translate(trans)
