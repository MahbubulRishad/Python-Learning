# print 1-10
for i in range (1,11):
    print(i)

# print all even number between 1 and 20
for evenNumber in range(2, 21, 2):
    print("Even numbers: ",evenNumber)

# find the sum of numbers from 1 to N
n = int(input("Enter a number: "))
total = 0
for i in range (0, n+1):
    total += i

print("Total: ", total)

# count how many vowels in given string
stringInput = input("Enter a string: ").lower()
count = 0
for char in stringInput:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print("Total Vowel Count: ", count)