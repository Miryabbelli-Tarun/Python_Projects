class Account:
    def __init__(self,acc_no,pin_number,name,balance):
        self.account_no=acc_no
        self.pin_number=pin_number
        self.name=name
        self.balance=balance 
        self.transactions=[]
    def show_balance(self):
        print(f'balance amount:{self.balance}')
        self.transactions.append('fetch the balance')
    def deposite(self,amount):
        self.balance+=amount
        print('Deposite succesfull')
        self.transactions.append(f'{amount} deposited')
    def withdraw(self,amount):
        if self.balance<amount or amount<0:
            print('insufficent balance')
        else:
            self.balance-=amount
            print('withdraw succesful')
            self.transactions.append(f"{amount} withdraw")
    def get_pin(self):
        return self.pin_number
    def show_transactions(self):
        if not self.transactions:
            print('no transactions yet!!')
            return
        print("-------Transactions history-----------")
        for transaction in self.transactions:
            print(f'{transaction}')
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

    def tranfer_amount(self,sender_acc_no,reciver_acc_no,amount):
        sender=self.get_account(sender_acc_no)
        reciver=self.get_account(reciver_acc_no)

        if not sender or not reciver:
            print('one account is not found please check account numbers')
            return
        if amount<0:
            print('invalid amount')
            return
        
        if sender.balance<amount:
            print('insuffecient fundes')
            return
        
        sender.balance-=amount
        reciver.balance+=amount
        print('money transfer succesfull')
        print(f'{amount} transferd from acount number {sender_acc_no} to {reciver_acc_no}')
        sender.transactions.append(f'{amount} transferd to {reciver_acc_no}')
        reciver.transactions.append(f"reciver {amount} from {sender_acc_no}")


def main():
    bank=Bank()
    while True:
        print('====================Bank system================')
        print('1.create account')
        print('2.show balance')
        print('3.deposit amount')
        print('4.withdraw amount')
        print('5.show all accounts')
        print('6.tranfer money ')
        print('7.show transaction history')
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
            pin_number=input('Enter pin number:')
            account=bank.get_account(acc_no)
            if account:
                if pin_number==account.get_pin():
                    account.withdraw(amount)
                else:
                    print('wrong pin')
        elif choice=='5':
            bank.show_all_accounts()
        elif choice=='6':
            sender_acc_no=int(input('Enter your account number:'))
            reciver_acc_no=int(input('Enter reciver account number:'))
            pin_number=input('Enter your pin number:')
            amount=int(input('Enter amount to send:'))
            account=bank.get_account(sender_acc_no)
            if account:
                if pin_number==account.get_pin():
                    bank.tranfer_amount(sender_acc_no,reciver_acc_no,amount)
                else:
                    print('wrong pin')
        elif choice=='7':
            acc_no=int(input('Enter your account number:'))
            pin_number=input('Enter pin number:')
            account=bank.get_account(acc_no)
            if account:
                if pin_number==account.get_pin():
                    account.show_transactions()
                else:
                    print('wrong pin')

        elif choice=='10':
            break
        else:
            print('invalid choice')

if __name__=='__main__':
    main()