i = 1
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)


while True:
    user_input = int(input("Enter a number: "))
    if user_input >2:
        print("Entered a valid input")
        break

    else:
        print(f"You entered {user_input}, an invalid input")

while True:
    user_email = input("Enter a email: ")
    user_password = input("Enter a password: ")

    if user_email == "abc@gmail.com" and user_password == "123admin":
        print("Successfully logged in")
        break

    else:
        print(f"Invalid credentials")