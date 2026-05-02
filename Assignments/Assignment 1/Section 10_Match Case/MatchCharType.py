inputChar = input("Enter a char: ")
match inputChar:
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
        print("Vowel")
    case _:
        if inputChar.isdigit():
            print("Digit")
        elif inputChar.isalpha():
            print("Consonant")
        else:
            print("Not a valid character")