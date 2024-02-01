import random
import sys
H_score = 0
C_score = 0
error_count = 0
move_list = ['rock', 'paper', 'scissors']
repeat = ['yes', 'no']
# STep 1:Define the base class
class Player:
    def __init__(self,name):
        self.name = name
    
    def choose_move(self):
        pass

# Step 2:Create a derived class (Human)  
class Human(Player):
    def choose_name(self):
        self.name = input("Please enter your name: ").lower()
    
    def choose_move(self):
        global error_count
        while True:
            move = input(f"{self.name}, Please enter your move." "\n Choose rock, paper or scissors: ").lower()
            if move in move_list:
                return move
            else:
                print("Invalid Choice")
                error_count += 1
                if error_count >= 3:
                    print("3 strikes and you're out, try again when you're ready")
                    sys.exit()
                    
        
# Step 3:Create a derived class (Com)  
class Com(Player):
    def choose_move(self):
        return random.choice(move_list)
        
# Step 4:Create a game class to manage gameplay   

class RockPaperScissors:
    # Create the characters
    def __init__(self):
        self.player1 = Human("")
        self.player2 = Com("Al Gorithm")
        
    def determine_winner(self, moveH, moveC):
        global H_score, C_score
        if moveH == moveC:
            return (f"It's a tie! You both played {moveH}. \n User Score: {H_score}, Al Gorithm Score: {C_score}")
        elif (moveH == "rock" and moveC == "scissors") or \
             (moveH == "scissors" and moveC == "paper") or \
             (moveH == "paper" and moveC == "rock"):
             H_score += 1
             return f"{self.player1.name} Wins \n User Score: {H_score},Al Gorithm Score: {C_score}"
        else:
            C_score += 1
            return f"{self.player2.name} Wins \n User Score: {H_score}, Al Gorithm Score: {C_score}"
        

    def play_game(self):
        # Intro
        print("Welcom to ROCk PAPER SCISSORS!!!!")
        # Call the choose_name method for the human player
        self.player1.choose_name()
        while True:
            global error_count
            # Call the move method on players
            moveH = self.player1.choose_move()
            moveC = self.player2.choose_move()
            # Display moves
            print(f"{self.player1.name} chose {moveH}")
            print(f"{self.player2.name} chose {moveC}")
            result = self.determine_winner(moveH, moveC)
            print(result)
            # Ask player if they want to continue playing
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == 'yes':
                    break
                elif play_again == 'no':
                    print("Thanks for playing. Goodbye!")
                    sys.exit()
                else:
                    print("Invalid choice")
                    error_count += 1
                    if error_count == 3:
                        print("3 strikes and your out,try again when your ready")
                        sys.exit()
                
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()