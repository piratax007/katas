def validate_input(n: int) -> int:
    if isinstance(n, float) or not (0 < n < 4000):
        raise ValueError("The input must be a positive integer")

    return n


def separate_into_digits(n: int) -> list:
    list_of_digits = [0, 0, 0, 0]

    for i, digit in enumerate(str(n)[::-1]):
        list_of_digits[3 - i] = int(digit)

    return list_of_digits


def assign_symbol(val: int, position: str) -> str:
    pivots = {
        "units": "I",
        "half_tens": "V",
        "tens": "X",
        "half_hundreds": "L",
        "hundreds": "C",
        "half_thousands": "D",
        "thousands": "M",
    }

    next_pivot = {
        "units": "tens",
        "tens": "hundreds",
        "hundreds": "thousands"
    }

    if val < 4:
        return pivots[position] * val

    if val == 4:
        return pivots[position] + pivots["half_" + next_pivot[position]]

    if val == 5:
        return pivots["half_" + next_pivot[position]]
    
    if 5 < val < 9:
        return pivots["half_" + next_pivot[position]] + pivots[position] * (val - 5)

    if val == 9:
        return pivots[position] + pivots[next_pivot[position]]


def roman_from(arabic_int: int) -> str:
    dec_int = separate_into_digits(validate_input(arabic_int))

    positions = {
        0: "thousands",
        1: "hundreds",
        2: "tens",
        3: "units"
    }

    roman_numeral = ""

    for i, integer in enumerate(dec_int):
        if dec_int[i] == 0:
            continue

        roman_numeral += assign_symbol(integer, positions[i])

    return roman_numeral
