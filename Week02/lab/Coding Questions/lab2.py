# Importing the random library to use for the dice later
import random

# Defining Variables
numLives = 10           # This is for number of player's lives remaining
mNumLives = 12          # This is for number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]

# Get the hero's combat strength with error handling
def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")

combatStrength = get_valid_int_input("Enter your combat Strength: ")
mCombatStrength = get_valid_int_input("Enter the monster's combat Strength: ")

# Roll the dice for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Weapons feature
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

input("Roll the dice to determine your weapon (Press enter)")
weaponRoll = random.randint(1, 6) - 1  # Adjusting for 0-based index
print(f"You rolled a {weaponRoll + 1}.")

# Add weapon roll to combat strength
combatStrength += weaponRoll

# Print hero's weapon and conditions
heroWeapon = weapons[weaponRoll]
print(f"Your weapon is: {heroWeapon}")

if weaponRoll + 1 <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll + 1 <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if heroWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Healing potion roll
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Equality operators
input("Analyze the roll (Press enter)")
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))
print("--- Phew, you have a healing potion: " + str(
    not (healthPoints < mCombatStrength) and healingPotion == 1))
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# Expanded if statement for health points
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

# Fight sequence
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your weapon (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
