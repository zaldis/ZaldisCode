from decimal import Decimal

from src.money import Money


class Wallet:
    def __init__(self) -> None:
        self._usd = Money("0")

    def withdraw(self, amount: 'Money') -> None:
        if self._usd < amount:
            raise ValueError("Not enough money!")
        self._usd -= amount

    def deposit(self, amount: 'Money') -> None:
        self._usd += amount

    def total_amount(self) -> Decimal:
        return self._usd.amount