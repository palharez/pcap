import threading
import random
import time

from typing import List


class Account:
    def __init__(self, balance=0) -> None:
        self.balance = balance


def service(accounts, total):
    for _ in range(1, 10_000):
        account1, account2 = select_two_accounts(accounts)
        value = random.randint(1, 100)
        transfer(account1, account2, value)
        bank_validate(accounts, total)


def create_accounts():
    return [
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
    ]


def transfer(source: Account, to: Account, value: int):
    if source.balance < value:
        return
    source.balance -= value
    time.sleep(0.001)
    to.balance += value


def bank_validate(accounts: List[Account], total: int):
    current = sum([account.balance for account in accounts])
    if current != total:
        print(
            f"Error with this total balance, {current:.2f} vs {total:.2f}", flush=True
        )
    else:
        print(f"Balanace, OK {current:.2f} vs {total:.2f}", flush=True)


def select_two_accounts(accounts):
    account1 = random.choice(accounts)
    account2 = random.choice(accounts)

    while account1 == account2:
        account2 = random.choice(accounts)

    return account1, account2


def main():
    accounts = create_accounts()
    total = sum(account.balance for account in accounts)
    print("Starting transfers")
    tasks = [
        threading.Thread(target=service, args=(accounts, total)),
        threading.Thread(target=service, args=(accounts, total)),
        threading.Thread(target=service, args=(accounts, total)),
        threading.Thread(target=service, args=(accounts, total)),
        threading.Thread(target=service, args=(accounts, total)),
        threading.Thread(target=service, args=(accounts, total)),
    ]
    [task.start() for task in tasks]
    [task.join() for task in tasks]
    print("Completed transfers")
    bank_validate(accounts, total)


if __name__ == "__main__":
    main()
