#Aiden Connolly
#W0478181 
#Prog1400
#Project:Bank_Account
#V.5
# Programming Language: Python 3
#Create a bank Account with dictionary
def create_account(owner, balance = 0):
    return {"owner": owner,"balance": balance}

def deposit(account, amount):
    account['balance'] += amount
    print(f"Deposited: ${amount}, New Balance: ${account['balance']}.") 
    
def withdrawal(account, amount):
    if amount <= account['balance']:
        account['balance'] -= amount
        print(f"Withdrew: ${amount}, New Balance: ${account['balance']}.")
    else:
        print("Insufficient Funds.")
        
def display_balance(account):
    print(f"Account Owner:{account['owner']}, Balance: ${account['balance']}")
    
#MAin
account1 = create_account("Jeffrey")
#Check the account
#print(account1)
display_balance(account1)
deposit(account1,1000)
withdrawal(account1,900)

print(type(account1))