import random

class Account:
    random.seed(87654321)
    def __init__(self, bank_id, name, surname):
        self.name = name
        self.surname = surname
        self.acc_numb = random.randint(10000, 99999) + (bank_id * 100000000)
        self.balance = 0
        self.history = list()


    def verify_balance(self):
        current_balance = sum(x[1] for x in self.history)
        if current_balance == self.balance:
            print('Balance confirmed: {self.balance}')
            return True
        else:
            print(f'Wrong balance: {self.balance} is not equal to the sum of operations ({current_balance})')
            return False


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
        dep = 0
        for x in self.accounts:
            if x.verify_balance:
                dep += x.balance
            else:
                print(f'Sorry, the deposit could not be calculated due to the problem with the account {x.acc_numb} of {x.name, x.surname}')
                return None
        return dep


    def add_account(self, name, surname):
        self.accounts.append(self.bank_id, Account(input('Input your name: '), input('Input your surname: ')))


    def transfer(self, from_acc, to_acc, amount):
        if abs(amount) == amount:
            self.transfers.append(WireTransfer(self.bank_id, from_acc, to_acc, amount))
            from_acc.balance -= amount
            from_acc.history.append((f'{from_acc} to {to_acc}', -amount))
            to_acc.balance += amount
            to_acc.history.append((f'{from_acc} to {to_acc}', amount))
        else:
            print(f'Wrong value! You cannot transfer {amount} because it is less than zero!')
