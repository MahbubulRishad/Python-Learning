languages = {'Python', 'Java', 'C++', 'TypeScript', 'C#', 'LaTex', 'HTML', 'Java', 'CSS', 'Ruby'}
for language in languages:
    print(language)

    if language == 'Java':
        languages.add('Php')
        break
print(languages)