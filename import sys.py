import sys

class BankAccount:
    num_accounts = 0

    def __init__(self, balance=0):
        BankAccount.num_accounts += 1
        self.owner = f"Account{BankAccount.num_accounts}"
        self.balance = balance

def create_account(accounts):
    account = BankAccount()
    accounts.append(account)
    print(f"Account created. Owner: {account.owner}")

def display_Balance(accounts):
    for account in accounts:
        print(f"{account.owner}: Balance - ${account.balance}")

def deposit(accounts):
    owner = input("Enter account owner: ")
    for account in accounts:
        if account.owner == owner:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            break
    else:
        print("Account not found.")

def withdrawal(accounts):
    owner = input("Enter account owner: ")
    for account in accounts:
        if account.owner == owner:
            amount = float(input("Enter withdrawal amount: "))
            account.withdrawal(amount)
            break
    else:
        print("Account not found.")

accounts = []

while True:
    user_input = input("""
        Welcome To Dyan Bryan Banking Services
        Please 
       
        1. Create Account
       
        2. Display Balance
       
        3. Make A Deposit
       
        4. Make a Withdraw

        5. Exit\n
        :""")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            create_account(accounts)
        elif user_input == 2:
            display_Balance(accounts)
        elif user_input == 3:
            deposit(accounts)
        elif user_input == 4:
            withdrawal(accounts)        
        elif user_input == 5:
            print('Thank You, Goodbye')
            break
        else:
            print("\nInvalid input.")
    else:
        print("\nInvalid input.")
