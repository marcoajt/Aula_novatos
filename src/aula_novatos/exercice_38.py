def max_path_sum(triangle: list[list[int]]) -> int:
    """Calcula a maior soma de cima até a base em um triângulo de números.

    Args:
        triangle (list[list[int]]): Triângulo de inteiros, onde cada linha
            tem exatamente 1 elemento a mais que a anterior.

    Returns:
        int: Maior soma possível do topo até a base.
    """
    partial = triangle.copy()

    for i in range(len(partial) - 2, -1, -1):

        for j in range(len(partial[i])):
            partial[i][j] += max(partial[i + 1][j], partial[i + 1][j + 1])

    return partial[0][0]
