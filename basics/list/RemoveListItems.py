programing = ['C#', 'Javascript', 'Typescript', 'Go', 'HTML']
programing.remove("C#")
print(programing)

programing.pop(2)
print(programing)

programing.pop()
print(programing)

programing.append("Python")
print(programing)

new_programming = ["HTML", "CSS", "Java"]
programing.extend(new_programming)
print(programing)

del programing[0]
print(programing)

programing.clear()
print(programing)