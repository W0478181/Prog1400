import random



#STep 1 define player 
class Weapon:
    def __init__(self, name, damage, ammo_cap):
        self.name = name
        self.damage = damage
        self.ammo_cap = ammo_cap
        self.ammo_remaining = ammo_cap
        
    def shoot(self):
        if self.ammo_remaining >= 0:
            print(F"{self.name} fired")
            
            
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None
        
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage}. {self.name}'s Health: {self.health}")
    
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped with {weapon.name}")
    
    def shoot(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print(f"{self.name} has no weapon!")
    
class Weapon:
    def __init__(self, name, damage, ammo_cap):
        self.name = name
        self.damage = damage
        self.ammo_cap = ammo_cap
        self.ammo_remaining = ammo_cap
        
    def shoot(self):
        if self.ammo_remaining >= 0:
            print(F"{self.name} fired")
            
class FPSGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def play_round(self):
        print("New Round!")
        self.player1.shoot()
        self.player2.take_damage(self.player1.weapon.damage)
        
        self.player2.shoot()
        self.player1.take_damage(self.player2.weapon.damage)
        
if __name__ == "__main__":
    #create weapon
    weapon_list = [
    Weapon("Assault Rifle", damage=10, ammo_cap=30),
    Weapon("Shotgun", damage=30, ammo_cap=8),
    Weapon("Rocket Launcher", damage=70, ammo_cap=1)
]
    assault_rifle  = Weapon("Assault Rifle",damage=10, ammo_cap=30)
    shotgun  = Weapon("Shotgun",damage=30, ammo_cap=8)
    rpg  = Weapon("Rocket Launcher",damage= 70, ammo_cap=1)
    #crate players
    player1 = Player("Player 1", health=100)
    player2 = Player("Player 2", health=100)   
    #equip weapons
    player1.equip_weapon(assault_rifle)
    player2.equip_weapon(shotgun)
    
    fps_game = FPSGame(player1,player2)
    fps_game.play_round()