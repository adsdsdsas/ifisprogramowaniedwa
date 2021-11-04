import random

class Account:
    random.seed(87654321)
    def __init__(self, bank_id, name, surname):
        self.name = name
        self.surname = surname
        self.acc_numb = random.randint(10000, 99999) + (bank_id * 100000000)            # sets the account number in format: [4 digits of bank ID, 5 random digits]
        self.balance = 0
        self.history = list()


    def verify_balance(self):
        current_balance = sum(x[1] for x in self.history)                               # sums every amount in self.history
        if current_balance == self.balance:                                             # if that sum is equal to self.balance
            print('Balance confirmed: {self.balance}')                                  # balance is confirmed
            return True
        else:
            print(f'Wrong balance: {self.balance} is not equal to the sum of operations ({current_balance})')
            return False                                                                # if not, we know that something is wrong and we need to check the history of operations


class WireTransfer:                                                                     # this is only a container for our transfer properties, used in bank.transfers, lines 37 and 58
    def __init__(self, bank_id, from_acc, to_acc, amount):
        self. bank_id = bank_id
        self. from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount


class Bank:
    random.seed(9999999)
    def __init__(self, name):
        self.bank_name = name
        self.bank_id = random.randint(1000, 9999)                                       # create 4 digits random bank ID
        self.accounts = list()
        self.transfers = list()


    @property                                                                           # @property decorator means that the method only calculates some values
    def deposit(self):
        dep = 0
        for x in self.accounts:                                                         # for every account
            if x.verify_balance:                                                        # verify balance and if verified
                dep += x.balance                                                        # add the balance to the sum of balances
            else:
                print(f'Sorry, the deposit could not be calculated due to the problem with the account {x.acc_numb} of {x.name, x.surname}')
                return None                                                             # if not verified we cannot calculate the deposit
        return dep


    def add_account(self, name, surname):
        new_account = Account(self.bank_id, input('Input your name: '), input('Input your surname: '))
        self.accounts.append(new_account)  # update the accouts list and create a new Account object


    def transfer(self, from_acc, to_acc, amount):
        if abs(amount) == amount:
            new_transfer = WireTransfer(self.bank_id, from_acc, to_acc, amount)
            self.transfers.append(new_transfer)                 # create a WireTranfer object and append it to the self.transfers list
            from_acc.balance -= amount
            from_acc.history.append((f'{from_acc} to {to_acc}', -amount))
            to_acc.balance += amount
            to_acc.history.append((f'{from_acc} to {to_acc}', amount))                                  # update both accounts balances and histories
        else:
            print(f'Wrong value! You cannot transfer {amount} because it is less than zero!')           # protect the amount from being negative
