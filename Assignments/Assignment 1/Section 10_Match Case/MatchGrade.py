

marks = int(input("Please enter your marks: "))

def match_rade(marks):
    if marks >= 90:
        return "A"
    elif 75 <= marks < 90:
        return "B"
    elif 60 <= marks < 75:
        return "C"
    else:
        return "F"

matchGrade = match_rade(marks)
match matchGrade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "F":
        print("Fail")
