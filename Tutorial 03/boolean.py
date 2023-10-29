#part A
"""bool1 = True 
bool2 = False

result_1 = bool1 and bool1
result_2 = bool1 and bool2
result_3 = bool2 and bool1
result_4 = bool2 and bool2

spam = 'Hello'
result_5 = 10 < 20 and spam == 'Hello'

print(">>> True and True:", result_1)
print(">>> True and False:", result_2)
print(">>> False and True:", result_3)
print(">>> False and False:", result_4)
print(">>> 10 < 20 and spam == 'Hello': ",result_5)"""

#part B
"""while True:
    try:
        m = int(input('Give me a number between 1 and 10: '))
        
        if 1 <= m <= 10:
            print('Well done! You gave me:', m)
            break  # Exit the loop when a valid number is entered
        else:
            print('The number is not in the range 1 to 10.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')"""

#part C
"""exp_1 = True or True
exp_2 = True or False
exp_3 = False or True
exp_4 = False or False
exp_5 = 10 > 20 or 20 > 10

print(">>> ",exp_1)
print(">>> ",exp_2)
print(">>> ",exp_3)
print(">>> ",exp_4)
print(">>> ",exp_5)"""

#part D
"""while True:
    try:
        exam_marks= int(input("Enter the exam mark: "))
        
        if 0 <= exam_marks <= 100:
            
            if exam_marks>= 70:
                print('Exceptional result!')
            elif exam_marks >= 40:
                print('Satisfactory result!')
            else:
                print('You have failed.')
            break  
        else:
            print("Invalid mark. Mark must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")"""

#part E
"""expression1 = not True
expression2 = not False
expression3 = not ('black' == 'white')

print(f'not True evaluates to {expression1}')
print(f'not False evaluates to {expression2}')
print(f'not ("black" == "white") evaluates to {expression3}')"""

#part F
"""while True:
    try:
        x = int(input("Enter a value for x: "))
        if not x > 10:
            print("not returned True")
        else:
            print("not returned False")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")"""
