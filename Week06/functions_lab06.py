import random

# Function to save game results to a file
def save_game_result(hero_won, short_name, num_stars):
    with open("save.txt", "a") as file:
        if hero_won:
            file.write(f"Hero {short_name} has killed a monster and gained {num_stars} stars.\n")
        else:
            file.write("Monster has killed the hero previously.\n")

# Function to load the last game result
def load_game_result():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(f"Previous game result: {last_line}")
                
                # Adjust combat strength based on last game result
                if "Hero" in last_line and "stars" in last_line:
                    stars = int(last_line.split()[-2])  # Extract stars count
                    return 1 if stars > 3 else 0  # Increase monster's strength if >3 stars
                elif "Monster" in last_line:
                    return -1  # Increase hero's strength if monster won
            else:
                print("No previous game results found.")
                return 0
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        return 0

# Function to get valid dream level input
def get_dream_level():
    while True:
        try:
            num_dream_lvls = int(input("How many dream levels do you want to go down? (Enter a number 0-3): "))
            if 0 <= num_dream_lvls <= 3:
                return num_dream_lvls
            else:
                print("Please enter a valid number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")

# Hero Attacks
def hero_attacks(combat_strength, m_health_points):
    print(f"Player's weapon ({combat_strength}) ---> Monster ({m_health_points})")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print(f"You have reduced the monster's health to: {m_health_points}")
    return m_health_points

# Monster Attacks
def monster_attacks(m_combat_strength, health_points):
    print(f"Monster's Claw ({m_combat_strength}) ---> Player ({health_points})")
    if m_combat_strength >= health_points:
        health_points = 0
        print("Player is dead")
    else:
        health_points -= m_combat_strength
        print(f"The monster has reduced Player's health to: {health_points}")
    return health_points
