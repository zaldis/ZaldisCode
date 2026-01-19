from decimal import Decimal


class Money:
    def __init__(self, amount: str|Decimal) -> None:
        _amount = Decimal(amount)
        if _amount < 0:
            raise ValueError("Money amount has to not negative.")
        self._amount = _amount

    def __sub__(self, other: 'Money') -> 'Money':
       return Money(self.amount - other.amount)

    def __add__(self, other: 'Money') -> 'Money':
        return Money(self.amount + other.amount)

    def __eq__(self, other: 'Money') -> bool:
        return self.amount == other.amount

    def __le__(self, other) -> bool:
        return self.amount <= other.amount

    def __lt__(self, other) -> bool:
        return self.amount < other.amount

    @property
    def amount(self) -> Decimal:
        return self._amount
