languages = {'Python', 'Java', 'C++', 'TypeScript', 'C#', 'LaTex', 'HTML', 'Java', 'CSS', 'Ruby'}
print(languages)

#remove item
languages.remove('C#')
print(languages)

# languages.remove('C#') #if item not found then raise issue
# print(languages)

languages.discard('C#') #if items not found then do not raise issue
print(languages)

#pop
removed_item = languages.pop()
print("Removed item:", removed_item)
print(languages)

#clear
languages.clear()
print(languages)

# del languages
# print(languages)