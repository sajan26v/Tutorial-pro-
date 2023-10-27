#exercise 05
"""for number in range(21):
    if number % 2 != 0:
        print(number)"""

#exercise 06
"""num_star = int(input("Enter the number of stars you want to display: "))
try:
    for _ in range(num_star):
        print("*", end=" ")
    print()
except ValueError:
    print("Inavild input. Try again")"""

#exercise 07
"""import random
try:
    num_rolls = int(input("Enter the number of times you want to roll the dice: "))
    double_count = 0
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll: {die1}, {die2}")
        
        if die1 == die2:
            double_count += 1
    print(f"Number of doubles rolled: {double_count}")
except ValueError:
    print("Invaild input. Please try again.")"""
