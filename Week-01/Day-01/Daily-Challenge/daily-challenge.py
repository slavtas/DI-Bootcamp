user_string = input('Please enter a string exactly 10 characters long')
if len(user_string) < 10:
    print('Your string is too short. Try again')
elif len(user_string) > 10:
    print('Your string is too long. Try again')
else:
    print('Congratulations! You\'ve written a perfect string!')
    print(f'First character: {user_string[0]}')
    print(f'Last character: {user_string[-1]}')
    for char in user_string:
        print(char)


import random
user_input = list('HelloWorld')
print(user_input)
random.shuffle(user_input)
print(user_input)
print(''.join(user_input))