# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }
# for key, value in my_books.items():
#     print(f'The key is {key} and the value is {value}')
    
#  # range() & enumerate()
# odd_numbers = list(range(1,20,2))
# print(odd_numbers)

# even_nums = []

# for i in range(1,20):
#     if i%2 == 0:
#         even_nums.append(i)

# print(even_nums)

# students = ['John', 'Anna', 'Kate', 'Mark']
# for index, name in enumerate(students):
#     print(index,name)
# students[1] = 'Maria'

# for index, name in enumerate(students):
#     students[index] = f'Hello {name}'
 
# print(students)

# for each_student in students:
#     if each_student == 'Hello Kate':
#         continue
#     else:
#         print(f'{each_student}, how are u?')

#pass

# if students[0] is 'Hello Harry':
#     pass
# else:
#     print('not Harry') 

# even_nums = []

# for i in range(1,20):
#     if i%2 == 0:
#         even_nums.append(i)
# print(even_nums)

# even_nums = [i for i in range(1,20) if i%2 == 0] # list comprehension, can also work with set {} but type should be added in print(type(even_nums))
# print(even_nums) # [] gives a list. {} gives a set. () gives a tuple

# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

# new_ages = {name:age +1 for (name,age) in family_age}

# print(new_ages)

# def say_hello():
#     print('Hello Python')
# say_hello() #calling the function

# def say_hello(greeting):
#     print(f'{greeting} Python')
# say_hello('Wassup')

# def say_hello(greetings):
#     name = input('What\'s your name?')
#     print(greetings, name)
# say_hello(Wassup)

# def say_hello(name,language):
#     if language == 'HE':
#         print(f'Shalom, {name}')
#     elif language == 'PT':
#         print(f'Ola, {name}')
#     elif language == 'RU':
#         print('Privet, {name}')
#     else:
#         print(f'{language} is not supported')
# say_hello('Slava', 'RU')

# # keyword argument
# say_hello(language = 'PT', name = 'Slava')
# say_hello(name='Slava')
# say_hello()
#  #Local and Global Scope

# def say_hello(greetings):
#     name = input('What\'s your name?')
#     print(greetings, name)

# global_var = 100

# def calculation(a,b):
#     global global_var
#     addition = a+b
#     substraction = a-b
#     global_var += addition
#     print(f'addition = {addition}\n substraction ={substraction}')
#     print(global_var)

#returning values
# global_var = 100

# def calculation(a,b):
    
#     addition = a+b
#     substraction = a-b
    
#     print(f'addition = {addition}\n')
#     return (addition, substraction)

# addition, substraction = calculation(8,10)

# total_value = 5

# def increase_total(addition,total_value):
#     result1 = total_value + addition
#     result2 = total_value - substraction
#     return (result1, result2)

# print(increase_total(addition,total_value))
import random
          
def get_random_temp(season):
    
    if season == 'winter':
        return random.randint(-10,14)
    elif season == 'spring' or 'fall':
        return random.randint(15,21)
    elif season == 'summer':
        return random.randint(22,40)

def main():
    season = input('Type in the season to know the temperature ')
    temperature = get_random_temp(season)
    print(f'The temperature right now is {temperature} degrees Celsius')

    if temperature < 0:
        print('Get back under the blanket and cancel all activities!')
    elif 0 <= temperature < 16:
        print('Don\'t forget your hat and coat!')
    elif 16 <= temperature <= 23:
        print('Seems like a great time to take a walk in the park!')
    elif 24 <= temperature < 32:
        print('Time to get your swimming suit and rush to the pool!')
    elif 32 <= temperature <= 40:
        print('Stay close to the AC unit and drink more water!')
main()