'''
Create accounts

Deposit money

Withdraw money

Check balance

Different account types

Secure balance handling
'''
from abc import ABC,abstractmethod

class Account(ABC):

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        self.__balance=amount
        print('balance is setted')
    
    def deposite(self,amount):
        self.__balance+=amount
        print('balance updated')

    @abstractmethod
    def withdraw(self):
        pass
class Savingaccount(Account):
    def withdraw(self,amount):
        if amount>self.get_balance():
            print('insufficent balance')
        else:
            new_balance=self.get_balance()-amount
            self.set_balance(new_balance)
            print('withdraw succesful')
class Currentaccount(Account):
    def withdraw(self,amount):
        new_balance=self.get_balance()-amount
        self.set_balance(new_balance)
        print('withdraw succesful')
class Bank:
    def __init__(self):
        self.accounts=[]
    def create_account(self,account):
        self.accounts.append(account)
        print(f'account created for {account.name}')
    def view_accounts(self):
        for acc in self.accounts:
            print(f"name:{acc.name}   | balance :{ acc.get_balance() }")



acc1=Savingaccount('tarun',2000)
acc2=Currentaccount('ravi',5000)
res=acc1.get_balance()
print(res)
acc1.withdraw(300)
res=acc1.get_balance()
print(res)
res=acc2.get_balance()
print(res)

b=Bank()
b.create_account(acc1)
b.create_account(acc2)
b.view_accounts()

        