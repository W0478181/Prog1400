#Aiden Connolly
#W0478181 
#Prog1400
#Project:BattleSim
#V.5
# Programming Language: Python 3

import time
import random
from character_creator import GenerateWeapon

def BestTwoOfThree(player, enemy):
    rounds = 0
    player_wins = 0
    enemy_wins = 0 

    while True:
        rounds += 1
        print(f"\nRound {rounds}  FIGHT")
       
        player["health"] = random.randint(25, 40)
        enemy["health"] = random.randint(25, 40)
        player["weapon"] = GenerateWeapon()
        enemy["weapon"] = GenerateWeapon()

        winner = runBattle(player, enemy)

        if winner == player:
            player_wins += 1
        elif winner == enemy:
            enemy_wins += 1

        if player_wins == 2: 
            print(f"\n{player['name']} wins after {rounds} rounds!")
            break
        
        elif enemy_wins == 2:
            print(f"\n{enemy['name']} wins after {rounds} rounds!")
            break

def runBattle(player, enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        player_attack = random.randint(0, player["weapon"]["Damage"])
        enemy_attack = random.randint(0, enemy["weapon"]["Damage"])
        while enemy["health"] <= 15 and enemy["health"] > 0:
            chance = (random.randint(1,100))
            potion = (random.randint(1,10))
            if chance < 20:
                enemy["health"] += potion
                print (f"\n{enemy['name']} has used a Health potion and regained {potion} Hp.")
                print(f"\n{enemy['name']}'s health: {enemy['health']}")
                
        while player["health"] <= 15 and player["health"] > 0:
            chance = (random.randint(1,100))
            potion = (random.randint(1,10))
            if chance < 20:
                player["health"] += potion
                print (f"\n{player['name']} has used a Health potion and regained {potion} Hp.")
                print(f"\n{player['name']}'s health: {player['health']}")

        if player_attack == 0:
            print(f"\n{player['name']} attacks {enemy['name']} with {player['weapon']['WeaponName']}")
            print(f"\n{player['name']} attack missed {enemy['name']}. {enemy['name']}'s health: {enemy['health']}")
            time.sleep(0.2)
        elif player_attack >= 6:
            print(f"\n{player['name']} hit a critical attack on {enemy['name']}  with {player['weapon']['WeaponName']} for {player_attack} damage. {enemy['name']}'s health: {enemy['health']}")    
            time.sleep(0.2)
        else:
            enemy["health"] = max(0, enemy["health"] - player_attack)
            print(f"\n{player['name']} attacks {enemy['name']} with {player['weapon']['WeaponName']} for {player_attack} damage. {enemy['name']}'s health: {enemy['health']}")
            time.sleep(0.2)

        if enemy_attack == 0:
            print(f"\n{enemy['name']} attacks {player['name']} with {enemy['weapon']['WeaponName']}")
            print(f"\n{enemy['name']} attack missed {player['name']}. {player['name']}'s health: {player['health']}")
            time.sleep(0.2)
        elif enemy_attack >= 6:
            print(f"\n{enemy['name']} hit a critical attack on {player['name']}  with {enemy['weapon']['WeaponName']} for {enemy_attack} damage. {player['name']}'s health: {player['health']}")
            time.sleep(0.2)
        else:    
            player["health"] = max(0, player["health"] - enemy_attack)
            print(f"\n{enemy['name']} counterattacks {player['name']}  with {enemy['weapon']['WeaponName']} for {enemy_attack} damage. {player['name']}'s health: {player['health']}")
            time.sleep(0.2)

    if enemy["health"] <= 0:
        print(f"\n{player['name']} has defeated {enemy['name']}")
        return player
    else:
        print(f"\n{enemy['name']} has defeated {player['name']}")
        return enemy