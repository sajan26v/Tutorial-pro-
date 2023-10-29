# Function to perform arithemic operations
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if  num2 == 0:
            return "Error: Divison By Zero"
        return num1 / num2
    else:
        return 

#Main calculator loop
while True:
    try:
        #Input from the user
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the an operator(+, -, *, /): ")
        num2 = float(input ("Eneter the second number: "))

        #Display the result 
        result = calculate(num1, operator, num2)
        print("Result: ", result)
    except ValueError:
        print("Invalid Input: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero")

    another_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
    if another_calculation != "y":
        break