#{'Python', 'Java', 'C++', 'TypeScript', 'C#', 'LaTex', 'HTML', 'java', 'CSS', 'Ruby'}
languages = {"Python", "C++", "Java", "TypeScript"}
print(languages)

#Add items
languages.add("Ruby")
print(languages)

if "Ruby" in languages:
    print(f"Present")
else:
    print(f"Not present")

#add multiple items using list
languages.update(["HTML", "CSS"])
print(languages)

#add multiple items using set
languages.update({"LaTex", "C#"})
print(languages)

languages.add("java") #Duplicates not allowed
print(languages)