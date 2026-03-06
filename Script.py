import random


def war(population, size, money, stability, structures):
    outcome = random.choice(["Super_win", "Win", "Lose", "Super_lose", "kingdom_done"])

    if outcome == "Super_win":
        structures += 1
        size += 100
        population += 30
        stability = 100
        print("You’ve conquered the kingdom!")

    elif outcome == "Win":
        size += 30
        money += 20
        population -= 30
        print("Your kingdom expanded!")

    elif outcome == "Lose":
        population -= 20
        size -= 15
        stability -= 20
        print("Your kingdom lost the war")

    elif outcome == "Super_lose":
        size -= 50
        stability -= 50
        population -= 50
        structures -= 1
        print("Your kingdom suffered a catastrophic loss!")

    elif outcome == "kingdom_done":
        print("Your kingdom was completely destroyed!")

    return population, size, money, stability, structures


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
    print("The actions are: famine, feed, growth, war, inflation, reform, build structure, rename")

    while True:
        action = input("Do something: ").lower()
        words = action.split()
        print(f"You did {action}")

        if action == "feed":
            population += 25
            money -= 10

        elif action == "growth":
            population += 35
            stability += 5

        elif "war" in words:
            population, size, money, stability, structures = war(
                population, size, money, stability, structures
            )

        elif action == "inflation":
            money += 100
            stability -= 30

        elif action == "reform":
            money -= 40
            stability += 30
            
        elif "rename" in action:
        	kingdom_name = input("rename your kingdom: ")
        	print(f"sucsessfully named. your kingdom renamed to {kingdom_name}")

        elif action.startswith("build"):
            if money >= 20:
                structures += 1
                money -= 20
                print("The structure has been built")
            else:
                print("Not enough money")

        else:
            print("Nothing happened")

        # Random plague
        if random.randint(1, 10) == 1:
            print("A mysterious plague hit your kingdom!")
            population -= 20
            stability -= 10

        # Rebellion
        if random.randint(1, max(1, stability)) == 1:
            print("A rebellion has hit your kingdom!")
            population -= 20
            population, size, money, stability, structures = war(
                population, size, money, stability, structures
            )

        # Prevent negatives
        population = max(0, population)
        size = max(0, size)
        money = max(0, money)
        stability = max(0, min(stability, 100))
        structures = max(0, structures)

        turn += 1
        money += 5  # taxes

        print(f"\nTurn: {turn}")
        print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}, Structures: {structures}")

        # Win condition
        if size >= 300 and structures >= 5:
            print("You formed an empire! You win!")
            break

        # Lose condition
        if population <= 0 or size <= 0 or money <= 0 or stability <= 0:
            print("Your empire has died!")
            break


game()