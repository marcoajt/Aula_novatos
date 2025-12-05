NUMBER_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand",
}


def number_to_words(n: int) -> str:
    """Convert number int to word

    Args:
        n (int): number for word

    Returns:
        str: word to count
    """
    text = ""

    if n in NUMBER_WORDS:
        return NUMBER_WORDS[n]

    if n >= 100:
        hundreds = n // 100
        rest = n % 100
        text = NUMBER_WORDS[hundreds] + "hundred"
        if not rest:
            return text
        text += "and"
        n = rest

    if n >= 20:
        tens = (n // 10) * 10
        units = n % 10
        text += NUMBER_WORDS[tens]
        if units > 0:
            text += NUMBER_WORDS[units]
    elif n > 0:
        text += NUMBER_WORDS[n]

    return text


def number_letter_count(limit: int) -> int:
    total = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        total += len(word)
    return total
