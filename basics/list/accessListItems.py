#list
list_of_programming_languages = ["Java", "Python", "C++", "Javascript"]
print(list_of_programming_languages)

#access a specific item
print(list_of_programming_languages[0])
print(list_of_programming_languages[2])

#negative indexing
print(list_of_programming_languages[-1]) #from last indexing

#range
print(list_of_programming_languages[1:3]) #output = start to end-1

#Check item
if "Python" in list_of_programming_languages:
    print(list_of_programming_languages.index("Python"), "Python is awesome")