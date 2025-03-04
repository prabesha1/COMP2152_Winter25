# lab 03

import random

# Setting up
# Creating a list of dice values from 1 to 6
diceOptions = list(range(1, 7))

# List of weapons corresponding to dice values
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

# Display available weapons with their indexes
print("Available Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")


# Input validation for hero's and monster's combat strength
def get_valid_strength(prompt):
    while True:  # Keep asking until valid input is provided
        try:
            value = int(input(prompt))  # Convert input to integer
            if 1 <= value <= 6:  # Check if it's between 1 and 6
                return value  # Return valid value
            else:
                print("Please enter a number between 1 and 6.")  # Out of range
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 6.")  # Not a number


# Get hero and monster strengths
combatStrength = get_valid_strength("Enter your combat strength (1-6): ")
mCombatStrength = get_valid_strength("Enter monster's combat strength (1-6): ")

# Battle simulation
print("\nStarting the battle!\n")
for j in range(1, 21, 2):  # Loop for rounds, odd numbers only (1, 3, ..., 19)
    # Rolling dice for hero and monster
    heroRoll = random.choice(diceOptions)  # Random dice roll for hero
    monsterRoll = random.choice(diceOptions)  # Random dice roll for monster

    # Adding dice rolls to the initial combat strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Announcing the results of the round
    print(f"Round {j}:")
    print(f"  Hero rolled {heroRoll}, selected {weapons[heroRoll - 1]}. Total Strength: {heroTotal}")
    print(f"  Monster rolled {monsterRoll}, selected {weapons[monsterRoll - 1]}. Total Strength: {monsterTotal}")

    # Determine the winner of the round
    if heroTotal > monsterTotal:
        print("  Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("  Monster wins the round!")
    else:
        print("  It's a tie!")

    # Check if it's round 11 to declare a truce
    if j == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break  # Exit the loop if a truce is declared
else:
    # This will execute if the loop completes without hitting the truce
    print("\nBattle complete! No truce was declared.")
