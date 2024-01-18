#Aiden Connolly
#W0478181 
#Prog1400
#Project:BattleSim
#V.5
# Programming Language: Python 3

from character_creator import GenerateAvatar
from battles import BestTwoOfThree
import sys

def play():
    player = GenerateAvatar()
    enemy = GenerateAvatar()
    BestTwoOfThree(player, enemy)
def again():    
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

if __name__ == "__main__":
    while True:
        play()
        if not again():
            sys.exit()