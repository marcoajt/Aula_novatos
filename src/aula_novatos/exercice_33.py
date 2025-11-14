def distance(strand2: str) -> int:
    """Hamming exercice

    Args:
        strand2 (str): strand2

    Raises:
        ValueError: length strand is diferent from length strand2

    Returns:
        int: return the quantity of different characters
    """

    diff = 0

    strand = "GAGCCTACTAACGGGAT"

    if len(strand) != len(strand2):
        raise ValueError("Strands must be of equal length.")

    for i in range(len(strand)):
        if strand[i] != strand2[i]:
            diff = 1 + diff

    return diff
