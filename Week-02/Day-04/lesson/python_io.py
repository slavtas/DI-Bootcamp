#old_school, mandatory -> manually close file
# try:
#     f = open('/courses/Week-02/Day-04/lesson/sample.txt', 'r')
#     content = f.read()
#     print(content)
# finally:
#     f.close()

#modern approach after py v2.5
import re

names = ['Darth','Luke','Lea']
occurences = {name: 0 for name in names}

with open(r'C:\Users\User\Desktop\DI-Bootcamp\Week-02\Day-04\lesson\starwars.txt', 'r', encoding='utf-8') as file:
    list_content = file.readlines()
    for line in list_content:
        print(line)
    # ex 2
    print('5th line', list_content[4])
    # ex3
    file.seek(4)
    fifth_character = file.read(1)
    print(fifth_character)
    # ex 4
    first_five = file.read(5)
    print(first_five)
    # ex 5
    content = file.read()
    words = content.split()
    print(words)
    # ex 6
    for name in names:
        occurences[name] = len(re.findall(rf'\b{name}\b', content))
    for name, count in occurences.items():
        print(f'{name}: {count} occurences')
    # ex 7
    with open(r'C:\Users\User\Desktop\DI-Bootcamp\Week-02\Day-04\lesson\starwars.txt', 'w', encoding='utf-8') as file:
    
        first_name='Slava'
        file.write(f'\n{first_name}')
    # ex 8
        add_last_name = re.sub(r'\bLuke\b', 'Luke SkyWalker', content)
        file.write(add_last_name)