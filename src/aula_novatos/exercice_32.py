# Grid e encontrar rotas para right e down, number of routes
def routes_grid(size: int) -> int:
    """Number of routes, exercice Euler 15

    Args:
        size (int): grid size

    Returns:
        int: number of routes
    """

    quant_inter = size + 1  # for node, example a grid 2x2 have 3x3 nodes

    dp = [
        [0 for _ in range(quant_inter)] for _ in range(quant_inter)
    ]  # Faz o grid de nodes

    for i in range(quant_inter):  # Definido os caminhos da coluna e da linha
        dp[i][0] = 1
        dp[0][i] = 1

    for i in range(1, quant_inter):  # Definindo o interio do grid
        for j in range(1, quant_inter):
            dp[i][j] = (
                dp[i - 1][j] + dp[i][j - 1]
            )  # Soma os caminhos da matriz de cima e da esquerda

    return dp[size][size]
