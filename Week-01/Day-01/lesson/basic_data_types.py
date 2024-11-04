#Basic Data Types: 

my_name = "Slava"
print(type(my_name))

some_variable = "35"
print(type(some_variable))


print (5+3)
my_bool = True
print(type(my_bool))


#STRINGS
greetings = "shabat shalom"
print('index of space:', greetings.index(''))
#indexing a string
print(greetings[3])

#slicing a string
print(greetings[2:5])
print(greetings[2::])
#-1 is the last index

#strings most used methods

print(len(greetings))
print(greetings[2:len(greetings)])

#strings most used methods

print ('hello'.capitalize())
print (greetings.capitalize())
print (greetings.title())

greetings = greetings.replace('shalom', 'meburah').title()

print(greetings)
#print(greetings_new)
print(greetings)

student = "  Harry Potter  "
student = student.strip()
print(student + greetings)
print(student + " " + greetings)
student = student.strip(' ')
student.replace('r', 'l')
print(student.replace('r','l') + 'hello')
print(student.replace('r', '') + ' hello')

#numbers: integer, float, complex numbers, boolean

int_num = 5 #int: whole numbers
float_num = 7.5

#OPERATIONS

print(int_num + float_num)

print(greetings * 10)
#\n jump one line \t spacing

print(round(5/3,2))
print(round(5/3,4))

print(13//2) #float division

print(13%2) #modulus

if 12%3 == 0:
    print('yes')

my_age = 39
print(my_age + 123879)

my_age = str(my_age)
print(type(my_age))

my_phone = '0539528662'
my_phone = int(my_phone)
print(type(my_phone))

#my_age = int(input('What is your age?'))
#print(type(my_age))

#if my_age < 18:
    #print("you can't drink vodka")
#else:
    #print('Uhuu let\'s celebrate')

#comparison operators
print(5 <= 7)
print(5 == 5)
print(5 <= 5)

#adding data types

f_name = 'Hermione'
l_name = 'Granger'
hermione_age = 15

#f string
print(f'Hello, {f_name} {l_name}, welcome to Hogwarts!')

print(f'Hello, {f_name} {l_name}, welcome to Hogwarts! Your age is {hermione_age}')

first_name = "Rick"
last_name = "Sanchez"

print(f"Hello, {first_name} {last_name}, where is Morty?")

#special characters \n (starts with new line) \t (gives tab spacing)
print(f'Hello world\nMy name is {first_name} {last_name}')
print(f'Hello world\tMy name is {first_name} {last_name}')

print('python' is "python")
print('python' is not "python")
print('html' is not 'css' and 'python' is 'python')
print('html' is not 'css' and 'python' is 'javascript')

# if 'html' is not 'css' and 'python' is 'javascript':
#     print('that\'s right!')
# #increment variable
# my_age = 39
# my_age -= 5
# print(my_age)

# age = input('how old are you?')
# print(f'You are {age} years old')

name_list = ['Harry', 'Hermione', 'Ron']
for name in name_list:
    print(name)
for i in range(3):
    print('Hello', i +1)

# Ask the user for a number between 1 and 100
number = int(input("Please enter a number between 1 and 100: "))

# Check if the number is within the range
if 1 <= number <= 100:
    # Check if the number is a multiple of both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of 3
    elif number % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of 5
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("The number is out of range. Please enter a number between 1 and 100.")

