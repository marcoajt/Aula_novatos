# Exercice Euler
# On txt file, order em alphabet names, characther name, sum on index valor of alphabet, and multiplicate of position name, after thar sum.

from pathlib import Path

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# TODO: PATHLIB, LAMBDA
# Pathlib para subtituir o filepath
# Lmbda para subtituir o def  dentro da def
# em vez de utilizar uma string para alphabet, utiliar um pacote chamado alphabet
# Outros alunos:
#   Ver sobre o ord para fazer a soma dos caractereres
#
# Curls para pegar o a o txt na internet.
# Celenium: Warning


def total_name_scores(file_path: str) -> int:
    """
    Args:
        file_path: Path to the .txt names file.
    Returns:
        Total of all name scores.
    """

    path = Path(file_path)  # Cria o objeto Path, this work on windows

    raw = path.read_text(encoding="utf-8")  # Lê tudo de uma vez

    raw = raw.replace('"', "").replace("\n", "").replace("\r", "")
    names = [n for n in raw.split(",") if n]

    names.sort()

    def alpha_value(name: str) -> int:

        return sum(ALPHABET.index(c) + 1 for c in name)

    return sum(
        (i + 1) * alpha_value(n) for i, n in enumerate(names)
    )  # enumarete(names, start=1) => Lina
