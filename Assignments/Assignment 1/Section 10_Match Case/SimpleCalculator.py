number1 = int(input("Please first number: "))
number2 = int(input("Please second number: "))
operator = input("Please enter operator: (+, -, *, /) ")
match operator:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case _:
        print("Invalid operator")

