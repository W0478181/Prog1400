import random
import time

class AmmunitionType:
    def __init__(self, name, damage_modifier):
        self.name = name
        self.damage_modifier = damage_modifier

class Weapon:
    def __init__(self, name, damage, ammo_cap, special_ability=None, critical_chance=0.1, ammunition_type=None):
        self.name = name
        self.damage = damage
        self.ammo_cap = ammo_cap
        self.ammo_remaining = ammo_cap
        self.special_ability = special_ability
        self.critical_chance = critical_chance
        self.ammunition_type = ammunition_type

    def shoot(self):
        if self.ammo_remaining > 0:
            self.ammo_remaining -= 1
            damage = self.damage

            # Modify damage based on ammunition type
            if self.ammunition_type:
                damage *= self.ammunition_type.damage_modifier

            # Check for critical hit
            if random.random() < self.critical_chance:
                damage *= 2
                print(f"Critical Hit! {self.name} dealt double damage!")

            print(f"{self.name} fired. Damage dealt: {damage}. Ammo remaining: {self.ammo_remaining}")

            # Trigger special ability
            if self.special_ability:
                self.special_ability()

            return damage
        else:
            print(f"{self.name} is out of ammo!")
            return 0

    def reload(self):
        self.ammo_remaining = self.ammo_cap
        print(f"{self.name} reloaded. Ammo restored to {self.ammo_cap}")

class Player:
    def __init__(self, name, health, position=(0, 0)):
        self.name = name
        self.health = health
        self.weapon = None
        self.score = 0
        self.stealth_mode = False
        self.position = position
        self.cover = None
        self.movement_speed = 1
        self.rounds_played = 0
        self.tactical_ability_cooldown = 0

    def take_damage(self, damage):
        if self.cover and self.cover.durability > 0:
            self.cover.take_damage(damage)
            print(f"{self.name} is behind {self.cover.name}.")
        else:
            self.health -= damage
            print(f"{self.name} took {damage} damage. {self.name}'s Health: {self.health}")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped with {weapon.name}")

    def shoot(self):
        if self.weapon and not self.stealth_mode:
            damage_dealt = self.weapon.shoot()
            self.score += damage_dealt
        elif self.stealth_mode:
            print(f"{self.name} is in Stealth Mode. Cannot shoot.")
        else:
            print(f"{self.name} has no weapon!")

    def reload_weapon(self):
        if self.weapon:
            self.weapon.reload()
        else:
            print(f"{self.name} has no weapon to reload!")

    def use_health_pack(self, health_pack_amount):
        self.health += health_pack_amount
        print(f"{self.name} used a health pack. Health restored to {self.health}")

    def enter_stealth_mode(self):
        self.stealth_mode = True
        print(f"{self.name} entered Stealth Mode.")

    def exit_stealth_mode(self):
        self.stealth_mode = False
        print(f"{self.name} exited Stealth Mode.")

    def move(self, direction):
        x, y = self.position
        if direction == "up":
            y += self.movement_speed
        elif direction == "down":
            y -= self.movement_speed
        elif direction == "left":
            x -= self.movement_speed
        elif direction == "right":
            x += self.movement_speed
        else:
            print("Invalid direction. Use 'up', 'down', 'left', or 'right'.")
            return

        self.position = (x, y)
        print(f"{self.name} moved to {self.position}.")

    def throw_grenade(self, target_player):
        if self.weapon and self.weapon.ammo_remaining > 0:
            damage = random.randint(20, 40)
            print(f"{self.name} threw a grenade at {target_player.name}. Damage dealt: {damage}")
            target_player.take_damage(damage)
            self.weapon.ammo_remaining -= 1
        else:
            print(f"{self.name} has no grenades!")

    def use_tactical_ability(self):
        if self.tactical_ability_cooldown == 0:
            print(f"{self.name} used a tactical ability!")
            # Add the tactical ability effect here
            self.tactical_ability_cooldown = 3  # Cooldown in rounds
        else:
            print(f"{self.name}'s tactical ability is on cooldown. Turns remaining: {self.tactical_ability_cooldown}")

    def update_cooldowns(self):
        if self.tactical_ability_cooldown > 0:
            self.tactical_ability_cooldown -= 1

class FPSGame:
    def __init__(self, player1, player2, max_rounds=10, round_timer=60, global_leaderboard=None):
        self.player1 = player1
        self.player2 = player2
        self.max_rounds = max_rounds
        self.round_number = 0
        self.round_timer = round_timer
        self.global_leaderboard = global_leaderboard
        self.ammo_types = [
            AmmunitionType("Armor-Piercing", 1.5),
            AmmunitionType("Explosive", 2.0),
            AmmunitionType("Hollow-Point", 0.8)
        ]

    def play_round(self):
        self.round_number += 1
        print(f"\n--- Round {self.round_number} ---")

        # Update player cooldowns
        self.player1.update_cooldowns()
        self.player2.update_cooldowns()

        # Random chance for health pack
        if random.random() < 0.2:
            health_pack_amount = random.randint(10, 30)
            print(f"A health pack appeared! {health_pack_amount} health restored.")
            self.player1.use_health_pack(health_pack_amount)
            self.player2.use_health_pack(health_pack_amount)

        # Random chance for ammo type change
        if random.random() < 0.2:
            ammo_type = random.choice(self.ammo_types)
            self.player1.weapon.ammunition_type = ammo_type
            self.player2.weapon.ammunition_type = ammo_type
            print(f"Ammo type changed to {ammo_type.name}.")

        # Random chance to enter or exit stealth mode
        if random.random() < 0.2:
            self.player1.enter_stealth_mode()
        elif random.random() < 0.2:
            self.player1.exit_stealth_mode()

        # Random chance for cover
        if random.random() < 0.2:
            cover = Cover("Concrete Barrier", durability=50)
            self.player1.cover = cover
            self.player2.cover = cover
            print(f"{cover.name} appeared on the battlefield.")

        # Random chance for movement
        if random.random() < 0.2:
            direction = random.choice(["up", "down", "left", "right"])
            self.player1.move(direction)
            self.player2.move(direction)

        # Random chance for tactical ability usage
        if random.random() < 0.1:
            self.player1.use_tactical_ability()

        if random.random() < 0.1:
            self.player2.use_tactical_ability()

        # Random chance for grenade throw
        if random.random() < 0.1:
            self.player1.throw_grenade(self.player2)

        if random.random() < 0.1:
            self.player2.throw_grenade(self.player1)

        self.player1.shoot()
        self.player2.take_damage(self.player1.weapon.damage)

        self.player2.shoot()
        self.player1.take_damage(self.player2.weapon.damage)

        self.check_winner()

    def check_winner(self):
        if self.player1.health <= 0 or self.player2.health <= 0 or self.round_number == self.max_rounds:
            self.display_winner()
            exit()

    def display_winner(self):
        print("\n--- Game Over ---")
        print("Final Scores:")
        print(f"{self.player1.name}: {self.player1.score} points")
        print(f"{self.player2.name}: {self.player2.score} points")

        if self.player1.health <= 0 and self.player2.health <= 0:
            print("It's a tie!")
        elif self.player1.health <= 0:
            print(f"{self.player2.name} wins!")
        elif self.player2.health <= 0:
            print(f"{self.player1.name} wins!")
        else:
            print("Game ended without a clear winner.")

# Special Abilities
def poison_ability():
    print("Poisoned! Target takes damage over time.")

def healing_ability():
    print("Healing! Player restores health.")

if __name__ == "__main__":
    # Create weapons with different ammunition types
    assault_rifle = Weapon("Assault Rifle", damage=10, ammo_cap=30, critical_chance=0.2)
    shotgun = Weapon("Shotgun", damage=30, ammo_cap=8, special_ability=poison_ability)
    rpg = Weapon("Rocket Launcher", damage=70, ammo_cap=1, special_ability=healing_ability)

    # Create players
    player1 = Player("Player 1", health=100)
    player2 = Player("Player 2", health=100)

    # Equip weapons
    player1.equip_weapon(assault_rifle)
    player2.equip_weapon(shotgun)

    # Create the game instance
    game = FPSGame(player1, player2, max_rounds=5)

    # Play multiple rounds
    while True:
        game.play_round()
        time.sleep(1)  # Add a delay between rounds for better visibility
