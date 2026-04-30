num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by 2 and 3")

else:
    print(f"{num} is not divisible by 2 and 3")