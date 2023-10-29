#Question 03
#part A
while True:
    try:
        choice = input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: ")
        
        if choice == '1':
            celsius = float(input("Enter a temperature in Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == '2':
              fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
              celsius = (fahrenheit - 32) / 1.8
              print(f"{fahrenheit}°F is equal to {celsius}°C")
        else:
            print("Invalid option entered. Please enter '1' or '2' for the conversion type.")
        break
    except ValueError:
        print("Invaild Input: Please Enter Again..")
        