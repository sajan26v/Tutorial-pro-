while True:
    try:
        choice = int(input("Choose an option (1 , 2, 3, or 4 to quit): "))

        if choice == 1:
            print("1 selected")
        elif choice == 2:
            print("2 selected")
        elif choice == 3:
            print("3 selected")
        elif choice == 4:
            print("Quit selected")
            break
        else:
            print("Option not recognized")
    except ValueError:
        print("Invaild input. Please enter again")
