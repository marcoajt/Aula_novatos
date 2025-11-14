def fibonnaci(number: int) -> int:

    if number <= 1:
        return number
    return fibonnaci(number - 1) + fibonnaci(number - 2)
