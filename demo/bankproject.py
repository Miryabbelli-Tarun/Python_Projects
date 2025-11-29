from abc import ABC,abstractmethod

#used for printing the transactions
class transaction_log:
    def log(self,message):
        print("[LOG]",message)

#basic account
class account(ABC):
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.__balance=balance
        self.logger=transaction_log()
    def deposite(self,amount):
        self.__balance+=amount
        self.logger.log(f"deposite amount debited current amount is {self.__balance}")

    @abstractmethod
    def withdrawl(self,amount):
        pass
    
    def get_balance(self):
        return self.__balance
    def update_balance(self,amount):
         self.__balance=amount

#withdrawl from saving account
class saving_account(account):
    def withdrawl(self, amount):
        if amount<=self.get_balance():
            self.update_balance(self.get_balance()-amount)
            self.logger.log(f"{amount} withdrawl succesful. current balance is {self.get_balance()}")
        else:
            print("insufficent of fundus")





#note:-cannot create object for the abstract class
sav_acc=saving_account(9493,10000)
sav_acc.withdrawl(500)
sav_acc.deposite(600)