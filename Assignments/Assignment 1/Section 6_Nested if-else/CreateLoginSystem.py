username = input("Enter your username: ")
if username == "admin":
    password = input("Enter your password: ")
    if password == "123":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid username or password")
