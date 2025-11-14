def prime_factor(number: int) -> int:
    if number < 2:
        return number

    p = 2
    while p * p <= number:
        if number % p == 0:
            number //= p
        else:
            p += 1

    return number
