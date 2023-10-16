# Question 01 
# Part a
try:
    n = int(input("Give me a number: "))
    if n == 100:
        print(n, "is equal to 100")
    elif n > 100:
        print(n, "is greater than 100")
    else:
        print(n, "is less than 100")
except ValueError:
    print("Invalid input. Please enter a valid number.")

#Part b
