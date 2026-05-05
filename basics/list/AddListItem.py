programming = ['Python', 'Java', 'C++']
print(programming)

programming.append('GOOGLE')
print(programming)

programming.insert(3, "CSS")
print(programming)

new_programming = ['Ruby', 'TypeScript']
print(new_programming)

programming.extend(new_programming)
print(programming)

numbers = [1, 2, 3, 4, 5, 6]

#join 2 list - using loop
for items in numbers:
    programming.append(items)
print(programming)

#copy list
no1 = [1, 2, 3]
no2 = [4, 5, 6]
no3 = [7, 8, 9]
no_copy = no2.copy()
print(no1)
print(no_copy)

