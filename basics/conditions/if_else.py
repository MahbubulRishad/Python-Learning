#if-else
salary = int(input("Enter your salary: "))

if salary < 10000:
    print("Junior QA")

elif salary >= 10001 and salary <= 35000:
    print("Mid SQA")

elif salary >= 35001 and salary <= 75000:
    print("Mid-Senior QA")

else:
    print("Senior QA")