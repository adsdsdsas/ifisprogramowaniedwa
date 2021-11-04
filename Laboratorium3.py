import random

class Account:
    random.seed(87654321)
    def __init__(self, bank_id, name, surname):
        self.name = name
        self.surname = surname
        self.acc_numb = random.randint(10000, 99999) + (bank_id * 100000000)
        self.balance = 0
        self.history = dict()


    def verify_balance(self):
        pass


class WireTransfer:
    def __init__(self, bank_id, from_acc, to_acc, amount):
        self. bank_id = bank_id
        self. from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount


class Bank:
    random.seed(9999999)
    def __init__(self, name):
        self.bank_name = name
        self.bank_id = random.randint(1000, 9999)
        self.accounts = list()
        self.transfers = list()


    @property
    def deposit(self):
        pass


    def add_account(self, name, surname):
        self.accounts.append(self.bank_id, Account(input('Input your name: '), input('Input your surname: ')))


    def transfer(self, from_acc, to_acc, amount):
        self.transfers.append(WireTransfer(self.bank_id, from_acc, to_acc, amount))
        from_acc.balance -= amount
        from_acc.history.add(f'{from_acc} to {to_acc}', amount)
        to_acc.balance += amount
        to_acc.history.add(f'{from_acc} to {to_acc}', amount)
