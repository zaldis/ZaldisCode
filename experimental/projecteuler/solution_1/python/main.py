import math
from typing import Generator


def get_sum_of_multiples(limit: int, *dividers: int) -> int:
    """ Get sum of multiples which are divisible at least by one of provided dividers

    The algorithm goes through each possible multiple and checks
    if this multiple is divisible by any of provided dividers.
    If there is at least one such divider, then sum such multiples.
    """
    sum_of_multiples = 0
    for multiple in range(2, limit):
        is_divided_multiple = False
        for divider in dividers:
            if multiple % divider == 0:
                is_divided_multiple = True
        if is_divided_multiple:
           sum_of_multiples += multiple
    return sum_of_multiples
print("Result from functional summarizer:", get_sum_of_multiples(1000, 2, 6, 8))


class MultiplesSummarizer:
    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._dividers: list[int] = []

    def add_divider(self, new_divider: int) -> 'MultiplesSummarizer':
        self._dividers.append(new_divider)
        return self

    def sum(self) -> int:
        sum_of_multiples = 0
        for multiple in self._get_multiples():
            if self._is_divided_multiple(multiple):
                sum_of_multiples += multiple
        return sum_of_multiples

    def _get_multiples(self) -> Generator[int, None, None]:
        for multiple in range(2, self._limit):
            yield multiple

    def _is_divided_multiple(self, multiple: int) -> bool:
        for divider in self._dividers:
            if multiple % divider == 0:
                return True
        return False


class OptimizedMultiplesSummarizer(MultiplesSummarizer):
    def sum(self) -> int:
        if len(self._dividers) == 1:
            return self._get_sum_divisible_by(self._dividers[0])
        elif len(self._dividers) == 2:
            divider1 = self._dividers[0]
            divider2 = self._dividers[1]
            total = self._get_sum_divisible_by(divider1) + self._get_sum_divisible_by(divider2)
            total -= self._get_sum_divisible_by(math.lcm(divider1, divider2))
        else:
            total = super().sum()
        return total

    def _get_sum_divisible_by(self, n: int) -> int:
        """ Return sum of multiples divisible by n.

        Let's imagine n=3 and limit=16.
        Then divisible multiples will be: sum(3, 6, 9, 12, 15) => 3 * (1 + 2 + 3 + 4 + 5).
        So it gives the formula: n * (p * (p+1) / 2), where p = (limit-1) // n.
        """
        max_multiplier = (self._limit-1) // n
        return n * (max_multiplier * (max_multiplier+1) // 2)

multiples_summarizer = OptimizedMultiplesSummarizer(1000)
print("Result from optimized summarizer:", multiples_summarizer
    .add_divider(2)
    .add_divider(6)
    .add_divider(8)
    .sum()
)