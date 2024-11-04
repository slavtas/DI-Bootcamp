age = input('how old are you?')
print(f'You are {age} years old')

if age > 18 and age < 35:
    print('you can enter')
elif age < 18 and age > 12:
    print('get your mom\'s approval')
else:
    print('you\'re good to go')