#Aiden Connolly
#W0478181 
#Prog1400
#Project:Bank_Account
#V.5
# Programming Language: Python 3

#Create a bank Account with Class
class BankAccount:
    #Contructor (__init__ method):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")
        
    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}.")
        else:
            print("Insufficient Funds.")
            
    def display_balance(self):
        print(f"Account Owner: {self.owner}, Balance: ${self.balance}")

account1 = BankAccount("Hawking")
account1.display_balance()
account1.deposit(1000)
account1.withdrawal(400)
account1.display_balance()
        

