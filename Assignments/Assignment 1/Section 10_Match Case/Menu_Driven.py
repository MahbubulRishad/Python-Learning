
    # Create a menu driven program
    # 1-> Add
    # 2-> Subtract
    # 3-> Exit

while True:
    number = int(input("Please enter a number (1/2/3): "))

    match number:
        case 1:
            input1 = int(input("Please enter first number: "))
            input2 = int(input("Please enter second number: "))
            print("Add:", input1 + input2)

        case 2:
            input1 = int(input("Please enter first number: "))
            input2 = int(input("Please enter second number: "))
            print("Subtract:", input1 - input2)

        case 3:
            print("Exiting the program")
            break

        case _:
            print("Invalid choice, try again")