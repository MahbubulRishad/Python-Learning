# Print odd-even
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Print pass-fail
marks = int(input("Enter a marks: "))
print("Pass") if marks>=40 else print("Fail")

# print maximum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
max_num = num1 if num1>num2 else num2
print(f"Max number between {num1} and {num2} is: {max_num}")

# print positive-negative
number = int(input("Enter a positive or negative number: "))
resultPositive = "Positive" if number>0 else "Negative"
print(resultPositive)

#Print divisible by 5
divisibleByFiveNumber = int(input("Enter a Number: "))
var = True if divisibleByFiveNumber % 5 == 0 else False
print(var)
