import random
import os
import time

# Attack Name Generator
def generate_attack_name():
    prefixes = ["Mighty", "Shadow", "Fiery", "Storm", "Cursed", "Divine", "Vicious", "Ancient", "Mystic", "Savage"]
    suffixes = ["Strike", "Slash", "Blast", "Curse", "Fury", "Smash", "Whirlwind", "Assault", "Storm", "Burst"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

# Monster Name Generator
def generate_monster_name():
    prefixes = ["Fury", "Dark", "Gloom", "Iron", "Shadow", "Blight", "Storm", "Dread", "Wraith", "Night"]
    suffixes = ["beast", "fiend", "lurker", "wraith", "troll", "demon", "dragon", "ogre", "ghost"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

# Generate Monster
def generate_monster():
    return {
        "Name": generate_monster_name(),
        "Health": random.randint(55, 255),
        "Speed": random.randint(5, 30),
        "Attack1Name": generate_attack_name(),
        "Attack2Name": generate_attack_name(),
        "SpecialAttackName": generate_attack_name()
    }

# Player Abilities
def generate_ability():
    abilities = ["Heal", "Double Strike", "Defend", "Fireball"]
    return random.choice(abilities)

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display Player Stats
def display_player_stats():
    clear_screen()
    print("\n--- Player Stats ---")
    for key, value in player_stats.items():
        if key == "Inventory":
            value = ', '.join(value) if value else "Empty"
        print(f"{key}: {value}")
    print()

# Roll D20
def rolld20():
    return random.randint(1, 20)

# Check if Player is Dead
def is_player_dead():
    return player_stats['Health'] <= 0

# Start Game
def start_game():
    # Reset player stats
    player_stats.update({
        'Health': random.randint(99, 200),
        'Speed': random.randint(5, 30),
        'Attack1': random.randint(5, 30),
        'Attack2': random.randint(5, 30),
        'sAttack': random.randint(10, 45),
        'Ability': generate_ability()
    })

    # Generate a new monster
    generate_new_monster()

    # Easter Eggs
    name = player_stats['Name'].lower()
    if name == "death":
        print("\nYour fate is already determined. You have died.")
        player_stats['Health'] = 0
    elif name == "sonic999":
        print("\nYou are too fast... Your speed is now extraordinary!")
        player_stats['Speed'] = 999
    elif name == "ojas":
        print("\nIt can't be you... Here's an extra 100 health.")
        player_stats['Health'] += 100
    elif name == "jesus":
        print("\nOur Savior Jesus is here!!! Immense health and speed granted!")
        player_stats['Health'] += 999999
        player_stats['Speed'] += 99999
    time.sleep(2)
    clear_screen()

# Generate New Monster
def generate_new_monster():
    global monster_stats
    monster_stats = generate_monster()

# Display Title Screen
def display_title_screen():
    clear_screen()
    print("\n" + "-" * 30)
    print("      WELCOME TO DUNGEON QUEST")
    print("-" * 30)
    input("\nPress Enter to Start the Game...")

# Display Main Menu
def display_menu():
    clear_screen()
    print("\n--- Main Menu ---")
    print("[1]: Load Dungeon")
    print("[2]: Rest")
    print("[3]: Flee")
    print("[4]: Explore")
    print("[5]: Use Item")
    print("[6]: Exit Game")

# Rest
def rest():
    clear_screen()
    print("\nYou rest and recover some health.")
    player_stats['Health'] = min(player_stats['Health'] + 50, 200)
    time.sleep(2)
    clear_screen()

# Flee
def flee():
    clear_screen()
    print("\nYou flee from the dungeon. Goodbye!")
    exit()

# Explore
def explore():
    clear_screen()
    print("\nYou explore the dungeon and encounter something!")
    encounter = random.choice(["Potion", "Gold", "Trap", "Map", "Monster"])

    if encounter == "Potion":
        print("You find a potion and restore 20 health.")
        player_stats['Health'] = min(player_stats['Health'] + 20, 200)
        player_stats['Inventory'].append("Potion")
    elif encounter == "Gold":
        print("You find some gold! Your speed increases.")
        player_stats['Speed'] += random.randint(1, 10)
        player_stats['Inventory'].append("Gold")
    elif encounter == "Trap":
        print("You triggered a trap! Lose 30 health.")
        player_stats['Health'] -= 30
    elif encounter == "Map":
        print("You find a map that reveals the monster's weaknesses.")
        player_stats['Inventory'].append("Map")
    elif encounter == "Monster":
        print("You encounter a hidden monster! Prepare to battle!")
        battle()

    time.sleep(2)
    clear_screen()

# Use Item
def use_item():
    if not player_stats['Inventory']:
        print("\nYou have no items to use.")
        time.sleep(2)
        return

    print("\nYour Inventory:")
    for i, item in enumerate(player_stats['Inventory'], 1):
        print(f"[{i}]: {item}")

    try:
        choice = int(input("\nChoose an item to use: ")) - 1
        if player_stats['Inventory'][choice] == "Potion":
            print("\nYou use a potion and restore 20 health.")
            player_stats['Health'] = min(player_stats['Health'] + 20, 200)
        elif player_stats['Inventory'][choice] == "Gold":
            print("\nYou use the gold to increase your speed by 5.")
            player_stats['Speed'] += 5
        elif player_stats['Inventory'][choice] == "Map":
            print("\nThe map shows a hidden path. You gain extra speed.")
            player_stats['Speed'] += 10
        player_stats['Inventory'].pop(choice)
    except (ValueError, IndexError):
        print("\nInvalid choice. You lost your turn.")

    time.sleep(2)
    clear_screen()

# Player Attack
def player_attack():
    print("\n--- Choose Your Attack ---")
    print(f"[1]: {monster_stats['Attack1Name']} (Damage: {player_stats['Attack1']})")
    print(f"[2]: {monster_stats['Attack2Name']} (Damage: {player_stats['Attack2']})")
    print(f"[3]: {monster_stats['SpecialAttackName']} (Damage: {player_stats['sAttack']})")
    print(f"[4]: {player_stats['Ability']} (Special Ability)")
    print(f"[5]: Inventory")

    choice = input("Choose your attack or action: ")
    if choice == "1":
        monster_stats['Health'] -= player_stats['Attack1']
        print(f"\nYou used {monster_stats['Attack1Name']} and dealt {player_stats['Attack1']} damage!")
    elif choice == "2":
        monster_stats['Health'] -= player_stats['Attack2']
        print(f"\nYou used {monster_stats['Attack2Name']} and dealt {player_stats['Attack2']} damage!")
    elif choice == "3":
        monster_stats['Health'] -= player_stats['sAttack']
        print(f"\nYou used {monster_stats['SpecialAttackName']} and dealt {player_stats['sAttack']} damage!")
    elif choice == "4":
        if player_stats['Ability'] == "Heal":
            player_stats['Health'] = min(player_stats['Health'] + 50, 200)
            print("\nYou used Heal and restored 50 health!")
        elif player_stats['Ability'] == "Double Strike":
            monster_stats['Health'] -= (player_stats['Attack1'] + player_stats['Attack2'])
            print(f"\nYou used Double Strike and dealt {player_stats['Attack1'] + player_stats['Attack2']} damage!")
        elif player_stats['Ability'] == "Defend":
            print("\nYou used Defend and reduced incoming damage by half this turn!")
        elif player_stats['Ability'] == "Fireball":
            monster_stats['Health'] -= (player_stats['sAttack'] + 20)
            print(f"\nYou used Fireball and dealt {player_stats['sAttack'] + 20} damage!")
    elif choice == "5":
        use_item()

# Monster Attack
def monster_attack():
    print(f"\nThe monster attacks!")
    player_damage = random.randint(5, 45)
    player_stats['Health'] -= player_damage
    print(f"\nThe monster dealt {player_damage} damage to you!")

# Battle Sequence
def battle():
    print("\nA wild monster appears!")
    print(f"\nMonster Name: {monster_stats['Name']}")
    print(f"Monster Health: {monster_stats['Health']}")
    print(f"Monster Speed: {monster_stats['Speed']}")

    while monster_stats['Health'] > 0 and player_stats['Health'] > 0:
        if player_stats['Speed'] >= monster_stats['Speed']:
            player_attack()
            if monster_stats['Health'] > 0:
                monster_attack()
        else:
            monster_attack()
            if player_stats['Health'] > 0:
                player_attack()

        time.sleep(1)
        clear_screen()

    if is_player_dead():
        print("\nYou have been defeated. Game Over.")
    else:
        print(f"\nYou defeated the {monster_stats['Name']}!")
        player_stats['Inventory'].append("Monster Trophy")
        time.sleep(2)
        generate_new_monster()

# Main Game Loop
def main():
    display_title_screen()
    player_stats['Name'] = input("Enter your character's name: ")
    start_game()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            battle()
        elif choice == "2":
            rest()
        elif choice == "3":
            flee()
        elif choice == "4":
            explore()
        elif choice == "5":
            use_item()
        elif choice == "6":
            print("\nThank you for playing!")
            break
        else:
            print("\nInvalid choice, try again.")

if __name__ == "__main__":
    # Initialize Player and Monster Stats
    player_stats = {
        "Name": "",
        "Health": 0,
        "Speed": 0,
        "Attack1": 0,
        "Attack2": 0,
        "sAttack": 0,
        "Ability": "",
        "Inventory": []
    }
    monster_stats = {}

    main()
