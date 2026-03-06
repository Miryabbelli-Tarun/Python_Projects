class Account:
    def __init__(self,acc_no,name,balance):
        self.account_no=acc_no
        self.name=name
        self.balance=balance 
    def show_balance(self):
        print(f'balance amount:{self.balance}')
    def deposite(self,amount):
        self.balance+=amount
        print('Deposite succesfull')
    def withdraw(self,amount):
        if self.balance<amount or amount<0:
            print('insufficent balance')
        else:
            self.balance-=amount
            print('withdraw succesful')
class Bank:
    def __init__(self):
        self.accounts={}
        self.next_acc_no=1001
    def create_account(self,name,balance):
        acc_no=self.next_acc_no
        self.next_acc_no+=1
        account=Account(acc_no,name,balance)
        self.accounts[acc_no]=account
        print('Account created succesfully')
        print(f'your account number is {acc_no}')
    def get_account(self,acc_no):
        if acc_no in self.accounts:
            return self.accounts[acc_no]
        else:
            print('account not found')
            return None
    def show_all_accounts(self):
        for acc in self.accounts.values():
            print(f'{acc.account_no}   | {acc.name} | {acc.balance}')


def main():
    bank=Bank()
    while True:
        print('====================Bank system================')
        print('1.create account')
        print('2.show balance')
        print('3.deposit amount')
        print('4.withdraw amount')
        print('5.show all accounts')
        print('10.exit')

        choice=input('Enter choice :')

        if choice=='1':
            name=input('Enter name:')
            balance=int(input('Enter balance:'))
            bank.create_account(name,balance)
        elif choice=='2':
            acc_no=int(input('Enter bank account number:'))
            account=bank.get_account(acc_no)
            if account:
                account.show_balance()
        elif choice=='3':
            acc_no=int(input('Enter bank account number:'))
            amount=int(input('Enter amount to deposite:'))
            account=bank.get_account(acc_no)
            if account:
                account.deposite(amount)
        elif choice=='4':
            acc_no=int(input('Enter bank account number:'))
            amount=int(input('Enter amount to withdraw:'))
            account=bank.get_account(acc_no)
            if account:
                account.withdraw(amount)
        elif choice=='5':
            bank.show_all_accounts()
        elif choice=='10':
            break
        else:
            print('invalid choice')

if __name__=='__main__':
    main()