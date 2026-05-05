programmings = ['Javascript', 'Typescript', 'Python', 'HTML', 'CSS', 'Java']
for programming in programmings:
    print(programming)

for programming in range(len(programmings)):
    print(f"index: {programming}: ", programmings[programming])

#shorthand
[print(programming) for programming in programmings]