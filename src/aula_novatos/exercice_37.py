def find_fewest_coins(coins: list[int], target: int):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    best = {0: []}

    for value in range(1, target + 1):
        best_solution = None

        for coin in coins:
            prev = value - coin
            if prev < 0:
                continue
            if prev not in best:
                continue

            candidate = best[prev] + [coin]

            if best_solution is None or len(candidate) < len(best_solution):
                best_solution = candidate

        if best_solution is not None:
            best[value] = best_solution

    if target not in best:
        raise ValueError("can't make target with given coins")

    return best[target][::-1]
