from bankAccount import bankAccount

class User:		
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account_balance = BankAccount(int_rate, balance)

    # def make_deposit(self, amount):
    #     self.account.make_deposit(100)
    
    
    # def make_withdrawal(self, amount):
    #     self.account.make_withdrawal(10)

    	
    
    # def display_user_balance(self):
    #     print(self.name)
    #     print(self.account_balance)

    # def transfer_money(self,other_user,amount):
    #     other_user.account_balance += amount
    #     self.account_balance -= amount

lana = User("lanatheo",0.02, 500)
# lana = bankAccount(0.02)

print(lana.account.account_balance)

