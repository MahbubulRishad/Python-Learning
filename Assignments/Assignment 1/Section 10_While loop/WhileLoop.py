#print 10 to 1
from math import factorial

num = 10
while num > 0:
    print(num)
    num -= 1


# find the factorial number
numFact = int(input("Enter a number: "))
factorialNumber = 1
while numFact > 0:
    factorialNumber *= numFact
    numFact -= 1
print("Factorial is: ", factorialNumber)

# Keep asking user input until they enter exit
while True:
    exitBtn = input("Enter text: ").lower()
    if exitBtn == "exit":
        print("Thank you....Goodbye")
        break
    elif exitBtn == "":
        print("Please enter a valid text")
    else:
        print(f"Invalid text: {exitBtn}")


