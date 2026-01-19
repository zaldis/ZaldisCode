from decimal import Decimal

from src import Account, BalanceTransferService


class TestBalanceTransferService:

    def test_balance_transfer(self):
        # GIVEN
        from_account = Account(1, Decimal(100))
        to_account = Account(2, Decimal(150))
        amount = Decimal(100)
        service = BalanceTransferService()

        # WHEN
        service.transfer(from_account, to_account, amount)

        # THEN
        assert from_account.amount == 0
        assert to_account.amount == 250

    def test_low_balance_transfer(self):
        pass
