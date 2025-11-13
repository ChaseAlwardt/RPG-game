import random

def battle(player):
    # Create a random enemy
    enemies = [
        {"name": "Goblin", "hp": 30, "attack": (5, 10)},
        {"name": "Skeleton", "hp": 40, "attack": (6, 12)},
        {"name": "Orc", "hp": 50, "attack": (8, 15)}
    ]
    enemy = random.choice(enemies)

    print(f"\nA wild {enemy['name']} appears with {enemy['hp']} HP!")

    # Battle loop
    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Run")
        choice = input("> ")

        if choice == "1":
            # Player attacks
            damage = random.randint(8, 15)
            enemy["hp"] -= damage
            print(f"You attack the {enemy['name']} for {damage} damage!")

            if enemy["hp"] <= 0:
                print(f"You defeated the {enemy['name']}!")
                xp_gain = random.randint(10, 25)
                player["xp"] += xp_gain
                print(f"You gained {xp_gain} XP!")
                break

            # Enemy attacks
            enemy_damage = random.randint(*enemy["attack"])
            player["hp"] -= enemy_damage
            print(f"The {enemy['name']} hits you for {enemy_damage} damage!")
            if player["hp"] <= 0:
                print("You were defeated...")
                player["hp"] = 0
                break

        elif choice == "2":
            print("You ran away safely!")
            break

        else:
            print("Invalid choice!")

    return player