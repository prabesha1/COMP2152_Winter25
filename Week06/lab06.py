# lab06.py
import random
import functions_lab06 as functions

# Load previous game result and adjust combat strength
adjustment = functions.load_game_result()

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Get valid Hero and Monster's Combat Strength
while True:
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if combat_strength.isdigit() and m_combat_strength.isdigit():
        combat_strength = int(combat_strength)
        m_combat_strength = int(m_combat_strength)
        if 1 <= combat_strength <= 6 and 1 <= m_combat_strength <= 6:
            break

    print("Invalid input. Please enter integers between 1 and 6.")

# Apply previous game adjustment
if adjustment == 1:
    m_combat_strength += 1  # Increase monster's strength
elif adjustment == -1:
    combat_strength += 1  # Increase hero's strength

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, (combat_strength + weapon_roll))
print(f"The hero's weapon is {weapons[weapon_roll - 1]}")

# Get valid dream level input
num_dream_lvls = functions.get_dream_level()

# Adjust combat strength if hero goes deeper into dream levels
if num_dream_lvls != 0:
    combat_strength += num_dream_lvls

# Fight Sequence
m_health_points = random.choice(big_dice_options)
health_points = random.choice(big_dice_options)

print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    
    if attack_roll % 2 != 0:
        input("You strike (Press enter)")
        m_health_points = functions.hero_attacks(combat_strength, m_health_points)
    else:
        input("The Monster strikes (Press enter)")
        health_points = functions.monster_attacks(m_combat_strength, health_points)

# Determine winner and save game result
if health_points > 0:
    print("Hero wins the battle!")
    functions.save_game_result(True, "Hero", 3)
else:
    print("Monster wins the battle!")
    functions.save_game_result(False, "Hero", 1)
