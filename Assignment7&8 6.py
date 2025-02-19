class Bank_Account:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"succsefuuly deposited {amount} now bank balance:{self.balance}")
        else:
            print("deposited amount must be positive")
        
    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f"succesfully withdrawn amount {amount} now bank balance {self.balance}")
            else:
                print("insufficient bank balance")
        else:
            print("amount must be positive")
    def display(self):
        print(f"Account number:{self.account_number}")
        print(f"bank balance:{self.balance}")

acc = Bank_Account("123456789")
acc.deposit(100)
acc.withdraw(50)
acc.display()
