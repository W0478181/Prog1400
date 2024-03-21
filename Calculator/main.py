import AdvancedCalculator
import sys
tries = 0
#Functions
#Users have 3 attempts anytime they must input information, If there are 3 invalid attempts they will get a message and program will shut down.
def attempts():
    global tries
    tries += 1
    if tries == 3:
        print("\n\nToo many failed attemps please try again later.")
        sys.exit()
#Using functions from the module

while True:
    user_input = input("""
        Welcome to Dyan Bryan Calculator 
        Select what you would like to do.
        
        1. Addition
        2. Subtracton
        3. Multiplication
        4. Division          
        5. Exponentiate
        6. Exit\n
        :""")
    #How Users input will pull functions
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            x = int(input("Enter a number:"))
            y = int(input("Enter a number:"))
            print(f"Answer:{AdvancedCalculator.Calculator.add(x, y)}")
        elif user_input == 2:
            x = int(input("Enter a number:"))
            y = int(input("Enter a number:"))
            print(f"Answer:{AdvancedCalculator.Calculator.sub(x, y)}")
        elif user_input == 3:
            x = int(input("Enter a number:"))
            y = int(input("Enter a number:"))
            print(f"Answer:{AdvancedCalculator.Calculator.mult(x, y)}")
        elif user_input == 4:
            x = int(input("Enter a number:"))
            y = int(input("Enter a number:"))
            print(f"Answer:{AdvancedCalculator.Calculator.div(x, y)}")   

        elif user_input == 5:
            base = int(input("Enter a number:"))
            exponent = int(input("Enter a number:"))
            print(f"Answer:{AdvancedCalculator.Calculator.expo(base, exponent)}")

        elif user_input == 6:
            print('Thank You, Goodbye')
            sys.exit()
        else:
            print("\nInvalid input.")
            attempts()    
    else:
        print("\nInvalid input.")
        attempts()