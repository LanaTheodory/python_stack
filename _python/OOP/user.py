
class User:		
    def __init__(self, name, email,account_balance=0):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_deposit(self, amount):
    	self.account_balance += amount
    
    def make_withdrawal(self, amount):
    	self.account_balance -= amount	
    
    # def display_user_balance(self):
    #     print(self.name)
    #     print(self.account_balance)

    def display_user_info(self):
        print(self.name)
        print(self.account_balance)

    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount


guido = User("Guido van Rossum", "guido@python.com")
lana = User("lana theo", "lana@th")
omar = User("Omar Alhaddar", "omar@al")
ghazal = User("ghazal s", "ghazal@ht", 50)
print(ghazal.account_balance)

ghazal.make_withdrawal(10)
print(ghazal.account_balance)

ghazal.display_user_info()

ghazal.make_deposit(1000)
ghazal.display_user_info()

ghazal.transfer_money(lana,50)
ghazal.display_user_info()
lana.display_user_info()


# lana.make_deposit(100)
# lana.make_deposit(150)
# print(lana.account_balance)
# guido.make_deposit(100)
# print(guido.account_balance)
# omar.make_deposit(100)
# guido.make_withdrawal(50)
# print(guido.account_balance)
# lana.make_withdrawal(50)
# lana.make_withdrawal(90)
# print(lana.account_balance)

# guido.display_user_balance()


# omar.transfer_money(lana, 90)
# print(omar.account_balance)
# print(lana.account_balance)

# lana.make_deposit(100)
# print(lana.account_balance)

# omar.make_deposit(100)
# omar.make_withdrawal(10)
# omar.make_withdrawal(10)
# omar.make_withdrawal(10)

# omar.display_user_balance()
