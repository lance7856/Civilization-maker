import random

kingdom_name = input("Enter your kingdom name: ")
population = 100
size = 50
money = 50
stability = 100
turn = 0

print(f"Your kingdom is {kingdom_name}")
print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}")
print("The actions are: famine, feed, growth, war, inflation, reform")

while True:
    action = input("Do something: ").lower()
    print(f"You did {action}")

    if "famine" in action:  
        population -= 40  
        stability -= 10  

    elif "feed" in action:  
        population += 25  
        money -= 10  

    elif "growth" in action or "grow" in action:  
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
        stability -= 50  

    elif "reform" in action:  
        money -= 40  
        stability += 30  
      
    else:  
        print("Nothing happened")  

    population = max(0, population)
    size = max(0, size)
    money = max(0, money)
    stability = max(0, min(stability, 100))  

    turn += 1  
    print(f"Turn: {turn}")  
    print(f"Population: {population}, Size: {size}, Money: {money}, Stability: {stability}")

    if size >= 300:  
        print("You formed an empire! You win!")  
        break  

    if population <= 0 or size <= 0 or money <= 0 or stability <= 0:  
        print("Your empire has died!")  
        break
