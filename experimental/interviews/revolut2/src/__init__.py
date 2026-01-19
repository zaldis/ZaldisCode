from decimal import Decimal
from threading import Lock


class Account :
    def __init__(self, id: int, amount: Decimal):
        self.id = id
        self.amount = amount
        self.lock = Lock()


class LowBalanceError(Exception): pass

class BalanceTransferService:
    def transfer(self, from_account: Account, to_account: Account, amount: Decimal) -> None:
        """
        1. Check that account is valid
        2. Check that a from account is not a to account
        """
        if from_account.amount < amount:
            # TODO: add meaningful exception type
            raise LowBalanceError("Account balance is lower than amount.")

        """
        1 -> 2: (1, 2)
        2 -> 3: (2, 3)
        3 -> 4: (3, 4)
        4 -> 1: (1, 4)
        """

        first_lock = from_account.lock if from_account.id < to_account.id else to_account.lock
        second_lock = to_account.lock if from_account.id < to_account.id else from_account.lock

        with (first_lock, second_lock):
            from_account.amount -= amount
            to_account.amount += amount
