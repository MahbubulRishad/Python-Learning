languages =('CSS', 'Java', 'LaTex', 'C#', 'English', 'Marathi', 'Telegu', 'TypeScript', 'Python', 'Ruby', 'HTML', 'C++', 'Bangla')
print(languages)

#change tuple value
#1st step: covert to list
change_tuple_to_list = list(languages)
print(change_tuple_to_list)

#2nd step: Add items
change_tuple_to_list.append('Chainess')
print(change_tuple_to_list)

#3rd step:update items
change_tuple_to_list[2] = 'LaTexx'
print(change_tuple_to_list)

#4th steps: convert to tuple
languages = tuple(change_tuple_to_list)
print(languages)
