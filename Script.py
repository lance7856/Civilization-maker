import random

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

    if "famine" in action:  
        population -= 20  
        stability -= 10  

    elif "feed" in action:  
        population += 25  
        money -= 10  

    elif "growth" in action:
        population += 35  
        stability += 5  

    elif "war" in action:  
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

    elif "inflation" in action:  
        money += 100  
        stability -= 30  

    elif "reform" in action:  
        money -= 40  
        stability += 30 

   if action.startswith("build"):
        print("The structure has been built")
        structures += 1
        money -= 20

    elif random.randint(1, 10) == 1:  # Random plague event
        print("A mysterious plague hit your kingdom!")
        population -= 20
        stability -= 10

    else:  
        print("Nothing happened")  

    # Prevent stats from going negative or exceeding limits
    population = max(0, population)
    size = max(0, size)
    money = max(0, money)
    stability = max(0, min(stability, 100))  

    turn += 1  
    print(f"Turn: {turn}")  
    print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}, Structures: {structures}")

    # Win condition
    if size >= 300 and structures >= 5:
        print("You formed an empire! You win!")  
        break  

    # Lose condition
    if population <= 0 or size <= 0 or money <= 0 or stability <= 0:  
        print("Your empire has died!")  
        break