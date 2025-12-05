# Sum of digits of 2**number
# 2**15 -> 26
# 2**1000 -> ?


def sum_numbers(value: int) -> int:
    return sum(int(digit) for digit in str(2 ** (value)))
