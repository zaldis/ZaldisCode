from concurrent.futures.thread import ThreadPoolExecutor
from decimal import Decimal

from src import Bank


def test_registration_of_single_account():
    bank = Bank()
    name = "Vasil"
    bank.register(name)

    bank.deposit(name, Decimal(100))

    assert bank.account_statement(name) == 100


def test_transfer_between_accounts():
    bank = Bank()
    vasil_name = "Vasil"
    ivan_name = "Ivan"
    oleg_name = "Oleg"
    bank.register(vasil_name)
    bank.register(ivan_name)
    bank.register(oleg_name)
    bank.deposit(vasil_name, Decimal(100))

    bank.transfer(vasil_name, ivan_name, Decimal(100))
    bank.transfer(ivan_name, oleg_name, Decimal(100))

    assert bank.account_statement(vasil_name).is_zero()
    assert bank.account_statement(ivan_name).is_zero()
    assert bank.account_statement(oleg_name) == Decimal(100)


def test_concurrent_transfer_race_condition():
    bank = Bank()
    vasil_name = "Vasil"
    ivan_name = "Ivan"
    oleg_name = "Oleg"
    vitia_name = "Vitia"
    nazar_name = "Nazar"
    names = [vasil_name, ivan_name, oleg_name, vitia_name, nazar_name]
    for name in names:
        bank.register(name)
    for name in names:
        if name != nazar_name:
            bank.deposit(name, Decimal(100))

    with ThreadPoolExecutor(max_workers=5) as thread_executor:
        for name in [vasil_name, ivan_name, oleg_name, vitia_name]:
            thread_executor.submit(
                bank.transfer, name, nazar_name, Decimal(100)
            )
    assert bank.account_statement(nazar_name) == Decimal(400)


def test_concurrent_transfer_to_myself__no_deadlock():
    bank = Bank()
    vasil_name = "Vasil"
    bank.register(vasil_name)
    bank.deposit(vasil_name, Decimal(100))

    with ThreadPoolExecutor(max_workers=5) as thread_executor:
        thread_executor.submit(
            bank.transfer, vasil_name, vasil_name, Decimal(100)
        )

    assert bank.account_statement(vasil_name) == Decimal(100)