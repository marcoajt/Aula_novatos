# Grid e encontrar rotas para right e down, number of routes
# Definido os caminhos da coluna e da linha
# Definindo o interior do grid
# Soma os caminhos da matriz de cima e da esquerda
def routes_grid(size: int) -> int:
    """Number of routes, exercice Euler 15

    Args:
        size (int): grid size

    Returns:
        int: number of routes
    """

    quant_inter = size + 1  # for node, example a grid 2x2 have 3x3 nodes

    dynamic_programming = [
        [0 for _ in range(quant_inter)] for _ in range(quant_inter)
    ]  # Faz o grid de nodes

    for i in range(quant_inter):
        dynamic_programming[i][0] = 1
        dynamic_programming[0][i] = 1

    for i in range(1, quant_inter):
        for j in range(1, quant_inter):
            dynamic_programming[i][j] = (
                dynamic_programming[i - 1][j] + dynamic_programming[i][j - 1]
            )

    return dynamic_programming[size][size]
