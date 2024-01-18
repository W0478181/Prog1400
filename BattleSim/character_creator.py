#Aiden Connolly
#W0478181 
#Prog1400
#Project:BattleSim
#V.5
# Programming Language: Python 3

import random
def GenerateAvatar():
    return {
        'name': AvatarName(),
        'weapon': GenerateWeapon(),
        'health': random.randint(25, 50)
    }
def AvatarName():
    with open('C:\\Users\\W0478181\\OneDrive - Nova Scotia Community College\\PROG1700\\Projects\\PROG1700Assignments\\BattleSim\\AvatarNames.txt') as names_file, open('C:\\Users\\W0478181\\OneDrive - Nova Scotia Community College\\Documents\\Titles.txt') as titles_file:
        names = names_file.read().splitlines()
        titles = titles_file.read().splitlines()
    name = random.choice(names)
    title = random.choice(titles)
    return f"{name} {title}"

def GenerateWeapon():
    with open('C:\\Users\\W0478181\\OneDrive - Nova Scotia Community College\\PROG1700\\Projects\\PROG1700Assignments\\BattleSim\\Weapons.txt') as weapons_file:
        weapons = [line.split() for line in weapons_file.read().splitlines()]
        
    weapon = random.choice(weapons)
    return {'WeaponName': weapon[0], 'Damage': int(weapon[1])}
