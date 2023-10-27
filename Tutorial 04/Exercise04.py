sum = 0

for x in range(5):
    try:
        num = float(input("Enter a number: "))
        sum += num
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The total of the 5 numbers is:", sum)