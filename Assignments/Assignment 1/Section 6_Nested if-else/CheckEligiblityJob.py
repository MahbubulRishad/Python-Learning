name = input("Enter your name: ")
age = int(input("Enter your age: "))
degree = input("Enter your degree: (yes/no)").lower()
if age>= 18:
    if degree == "yes":
        print(f"Congratulations {name}, You are eligible for job")
    else:
        print("You are not eligible for job as you dont have any degree")
else:
    print(f"Sorry Mr.{name} You are not eligible for job")