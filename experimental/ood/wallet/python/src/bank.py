from decimal import Decimal

from src.account import Account


class Bank:
    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def register(self, name: str) -> None:
        if name in self._accounts:
            raise ValueError("Account with this name already exists.")
        self._accounts[name] = Account(name)

    def transfer(self, from_name: str, to_name: str, amount: Decimal) -> None:
        if from_name == to_name:
            raise ValueError("It's prohibited to transfer to yourself!")

        from_account = self._accounts[from_name]
        to_account = self._accounts[to_name]
        asc_first_name, asc_second_name = sorted([from_name, to_name])

        with (
            self._accounts[asc_first_name].lock,
            self._accounts[asc_second_name].lock
        ):
            from_account.withdraw(amount)
            to_account.deposit(amount)

    def deposit(self, name: str, amount: Decimal) -> None:
        account = self._accounts[name]
        with account.lock:
            account.deposit(amount)

    def withdraw(self, name: str, amount: Decimal) -> None:
        account = self._accounts[name]
        with account.lock:
            account.withdraw(amount)

    def account_statement(self, name: str) -> Decimal:
        account = self._accounts[name]
        return account.statement()
