from decimal import Decimal
from threading import Lock

from src.money import Money
from src.wallet import Wallet


class Account:
    def __init__(self, name: str) -> None:
        self._name = name
        self._wallet = Wallet()
        self.lock = Lock()

    def withdraw(self, amount: Decimal) -> None:
       self._wallet.withdraw(Money(amount))

    def deposit(self, amount: Decimal) -> None:
        self._wallet.deposit(Money(amount))

    def statement(self) -> Decimal:
        return self._wallet.total_amount()
