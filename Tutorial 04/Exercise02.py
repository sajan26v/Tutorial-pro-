total = 0
count = 0

while True:
    try:
        score = int(input("Enter score, (Enter -9 to end): "))
        if score == -9:
            if count > 0:
                average = float(total) / count
                print("Class avearge is", average)
            else:
                print("At least one score must be entered before calculating the average.")
            break
        total += score
        count += 1
    except ValueError:
        print("Invaild input. Please enter a vaild Number!. ")