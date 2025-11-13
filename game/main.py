from database import savePlayer, loadPlayer
from battle import battle

def main():
    player = loadPlayer() or {"name": "Hero", "hp": 100, "xp": 0}
    print(f"Welcome, {player['name']}!")  
    while True:
        print("\n1. Battle\n2. Save & Quit")
        choice = input("> ")
        if choice == "1":
            battle(player)
            player['xp'] += 10
        elif choice == "2":
            savePlayer(player)
            print("Progress saved!")
            break

if __name__ == "__main__":
    main()