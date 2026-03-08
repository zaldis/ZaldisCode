from enum import IntEnum
from typing import Sequence


class NumberSystem(IntEnum):
    BINARY = 2
    OCTAL = 8
    DECIMAL = 10
    HEXADECIMAL = 16


def encode_number(number: int, base: NumberSystem) -> Sequence[int]:
    encoded_number = []
    while number >= base:
        encoded_number.append(number % base)
        number //= base
    if number > 0:
        encoded_number.append(number)
    return encoded_number[::-1]

def validate_encoded_number(encoded_number: Sequence[int], base: NumberSystem) -> None:
    result = 0
    trace = []
    for power, coefficient in enumerate(reversed(encoded_number)):
        result += base ** power * coefficient
        trace.append(f"{coefficient} * {base}^{power}")
    print(' + '.join(trace) + f' = {result}')

def printable_number(encoded_number: Sequence[int]) -> str:
    return ''.join(map(_convert_number_to_base_digit, encoded_number))

def _convert_number_to_base_digit(number: int) -> str:
    if number < 9:
        return str(number)
    shift_from_a = number - 10
    return chr(ord('a') + shift_from_a)

if __name__ == '__main__':
    print("Decimal:", 823947193478)
    encoded_number = encode_number(823947193478, NumberSystem.HEXADECIMAL)
    print("Hexadecimal:", printable_number(encoded_number))
    validate_encoded_number(encoded_number, NumberSystem.HEXADECIMAL)

    # print("Decimal:", 2373)
    # encoded_number = encode_number(2373, NumberSystem.BINARY)
    # print("Binary:", printable_number(encoded_number))
    # validate_encoded_number(encoded_number, NumberSystem.BINARY)
