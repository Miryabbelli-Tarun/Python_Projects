class Account:
    def __init__(self,acc_no,pin_number,name,balance):
        self.account_no=acc_no
        self.pin_number=pin_number
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
    def get_pin(self):
        return self.pin_number
class Bank:
    def __init__(self):
        self.accounts={}
        self.next_acc_no=1001
    def create_account(self,pin_number,name,balance):
        acc_no=self.next_acc_no
        self.next_acc_no+=1
        account=Account(acc_no,pin_number,name,balance)
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
            print(f'{acc.account_no} |{acc.pin_number}   | {acc.name} | {acc.balance}')


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
            pin_number=input('Enter pin number:')
            balance=int(input('Enter balance:'))
            bank.create_account(pin_number,name,balance)
        elif choice=='2':
            acc_no=int(input('Enter bank account number:'))
            pin_number=input('Enter pin number:')
            account=bank.get_account(acc_no)
            if account:
                if pin_number==account.get_pin():
                    account.show_balance()
                else:
                    print('wrong pin number')
        elif choice=='3':
            acc_no=int(input('Enter bank account number:'))
            amount=int(input('Enter amount to deposite:'))
            pin_number=input('Enter pin number:')
            account=bank.get_account(acc_no)
            if account:
                if pin_number==account.get_pin():
                    account.deposite(amount)
                else:
                    print('Wrong pin')
        elif choice=='4':
            acc_no=int(input('Enter bank account number:'))
            amount=int(input('Enter amount to withdraw:'))
            pin_number=input('Enter pin number')
            account=bank.get_account(acc_no)
            if account:
                if pin_number==account.get_pin():
                    account.withdraw(amount)
                else:
                    print('wrong pin')
        elif choice=='5':
            bank.show_all_accounts()
        elif choice=='10':
            break
        else:
            print('invalid choice')

if __name__=='__main__':
    main()