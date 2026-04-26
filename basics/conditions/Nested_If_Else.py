# Nested if else
age = int(input("Enter your age: "))
voterArea = input("Enter your voter area: ")

if (age >= 18):
    if voterArea == "SHERPUR" or voterArea == "Sherpur" or voterArea == "sherpur":
        print("Your are allowed to vote in Sherpur")

    elif voterArea == "SYLHET" or voterArea == "Sylhet" or voterArea == "sylhet":
        print("Your are allowed to vote in Sylhet")

    elif voterArea == "DHAKA" or voterArea == "Dhaka" or voterArea == "dhaka":
        print("Your are allowed to vote in Dhaka")

    else:
        print(f"Your are not allowed to vote in {voterArea}")


else:
    print(f"Your are not allowed to vote")


