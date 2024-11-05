#Exercise_1 Convert lists into dictionaries via zip

keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

#Exercise_2 Cinemax v2.0

member = ['rick', 'beth', 'morty', 'summer']
ages = [43, 13, 5, 8]

family = dict(zip(member, ages))

print(family)

total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    
    total_cost += cost
    print(f'{member}: ${cost}')

print(f'Total cost for family: ${total_cost}')

# Bonus portion

family_dict = {}

while True:
    name = input('Enter family member, press "done" when finished: ')
    if name == 'done':
        break
    age = int(input(f'Enter {name}\'s age: '))
    family_dict[name] = age

print("\nFamily:", family_dict)

total_cost = 0

for member, age in family_dict.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    
    total_cost += cost
    print(f'{member}: {cost}')

print(f'Total cost for family: {total_cost}')

# Exercise_3 Zara Paradox

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
        }
    }
print(brand)

brand['number_stores'] = 2 # changed number of stores to "2"
print(brand)

print('Zara\'s clients are ', ', '.join(brand['type_of_clothes'])) #how to remove [] join()
# print(" ,".join(brand['type_of_clothes']))
brand['country_creation'] = 'Spain'
print(brand)

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
print(brand)

del brand['creation_date']
print(brand)

brand['international_competitors'].pop(-1)
print(brand)

print('Major colors in US are ',', '.join(brand['major_color']['US'])) #how to remove []

print('Amount of key value pairs are ', len(brand))

print('Keys of the dictionary are ',', '.join(brand.keys()))

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara) # "number_stores" was updated from 7000 to 10000, "creation_date" was added to the end of the dictionary since it was deleted previously
print(brand)

print(brand['number_stores']) #now it's 10000

# Exercise_4 Disney Characters

users = ['Mickey','Minnie','Donald','Ariel','Pluto']

# disney_users_A recreate {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4} name to index

disney_users_A = {}
for index in range(len(users)):
    disney_users_A[users[index]] = index

print(disney_users_A)

# disney_users_B recreate {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"} index to name

disney_users_B = {}
for index in range(len(users)):
    disney_users_B[index] = users[index]

print(disney_users_B)

# disney_users_C recreate {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4} sorted alphabetically

sorted_users = sorted(users)

disney_users_C = {}
for index, user in enumerate(sorted_users):
    disney_users_C[user] = index

print(disney_users_C)

