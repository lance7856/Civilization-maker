import random

def game():
    kingdom_name = input("Enter your kingdom name: ")
    population = 100
    size = 50
    money = 50
    stability = 100
    turn = 0
    structures = 0

    print(f"Your kingdom is {kingdom_name}")
    print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}")
    print("The actions are: famine, feed, growth, war, inflation, reform, build structure")

    while True:
        action = input("Do something: ").lower()
        print(f"You did {action}")

        if action == "famine":
            population -= 20
            stability -= 10

        elif action == "feed":
            population += 25
            money -= 10

        elif action == "growth":
            population += 35
            stability += 5

        elif action == "war":
            if random.choice([True, False]):
                size += 30
                money += 20
                population -= 30
                print("Your kingdom expanded!")
            else:
                size -= 30
                stability -= 20
                population -= 50
                print("Expansion failed, your kingdom shrank!")

        elif action == "inflation":
            money += 100
            stability -= 30

        elif action == "reform":
            money -= 40
            stability += 30

        elif action.startswith("build"):
            print("The structure has been built")
            structures += 1
            money -= 20

        else:
            print("Nothing happened")

        # 🎲 Random plague event (separate from action system)
        if random.randint(1, 10) == 1:
            print("A mysterious plague hit your kingdom!")
            population -= 20
            stability -= 10

        # Prevent negatives / limit stability
        population = max(0, population)
        size = max(0, size)
        money = max(0, money)
        stability = max(0, min(stability, 100))

        turn += 1
        print(f"\nTurn: {turn}")
        print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}, Structures: {structures}")

        # 🏆 Win condition
        if size >= 300 and structures >= 5:
            print("You formed an empire! You win!")
            break

        # 💀 Lose condition
        if population <= 0 or size <= 0 or money <= 0 or stability <= 0:
            print("Your empire has died!")
            break

game()