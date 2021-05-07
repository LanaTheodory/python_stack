

class bankAccount:
    def __init__(self,int_rate, account_balance=0):
        self.int_rate = int_rate
        self.account_balance = account_balance
    
    def make_deposit(self, amount):
        self.account_balance = self.account_balance + amount

    def make_withdrawal(self,amount):
        if amount < self.account_balance:
            self.account_balance = self.account_balance - amount
        else:
            print("you are broke!")

    def display_account(self):
        print(" your account balance is:" ,(self.account_balance))
        print(f" the interest rate is:{self.int_rate}")

    def interest_yeild(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * int_rate)



account1 = bankAccount(0.1,500)
print(account1.account_balance)

account1.make_deposit(150)

account1.make_withdrawal(50)

account1.display_account()

# account1.interest_yeild()