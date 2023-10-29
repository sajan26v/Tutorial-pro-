while True:
    try:
        #Ask the diner cost of meal
        meal_cost = float(input("Enter the costof the meal: $"))
    
        #Ask the diner satisfaction level
        satisfaction_level = int(input("Rate the satisfaction ( 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))
    
        #calculate the tip based on satisfaction level 
        if satisfaction_level == 1:
            tip_percentage = 0.20
            satisfaction_message = "Totally Satisfied"
    
        elif satisfaction_level == 2:
           tip_percentage = 0.15
           satisfaction_message = "Satisfied"

        elif satisfaction_level == 3:
           tip_percentage = 0.10
           satisfaction_message = "Dissatisfied"

        else:
           print("Invalid satisfaction level. Please enter 1, 2, or 3.")
           continue

       #claculate the tip 
        tip_amount = meal_cost * tip_percentage

       #report the satisfaction level and tip
        print(f"You are {satisfaction_level}.")
        print(f"Your tip amount is: ${tip_amount:.2f}")
        break
    except ValueError:
        print("Invalid input. Please enter again")