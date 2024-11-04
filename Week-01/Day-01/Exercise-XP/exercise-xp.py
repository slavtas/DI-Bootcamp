#Hello world exercise-1
print('Hello, world\n'*4)

#Math exercise-2
print((99**3)*8)

#Output exercise-3
print(5 < 3) #Output -> False
print(3 == 3) #Output -> True
print(3 == "3") #Output -> False, because 3 is an integer, and "3" is a string
# print("3" > 3) #Output Unknown since it's not a valid code, in order to run the comparisson string "3" must be converted via int() function. The valid code looks like this 
int("3") > 3, #Output result -> False
print("Hello" == "hello") #Output -> False, since in Python values are case sensitive, therefore it makes 'Hello' and 'hello' two different objects not equal in properties

#Computer Brand exercise-4
computer_brand = 'MSI'
print(f'I have a {computer_brand} computer')

#My Info exercise-5
name = 'Slava'
age = '39'
shoe_size = '41'
info = f'My name is {name} and I am {age} years old. In two years myage will match my shoe size which happens to be {shoe_size}.'
print(info)

#A & B exercise-6
a = 5 #enter any number
b = 7  #enter any number
if a > b:
    print('Hello, world!')
else:
    print('Try again!')

#Odd or Even exercise-7
number = int(input('Please enter a number'))
if number % 2 == 0:
    print('This one is even!')
else:
    print('Now that\'s odd!')

#Name please exercise-8
my_name = 'Slava'
name_pls = input('Tell me my name, please')

if name_pls == my_name:
    print('Congratulations! You have saved the world!')
else:
    print('Too bad, Griffindor loses 100 points!')

#High Enough? exercise-9
height = int(input('Are you tall enough? Please enter your height'))
if height <= 145:
    print('You are not tall enough, go back home and grow a couple of cm!')
else:
    print('Enjoy your ride, you magnificent Tour d\'Eiffel!')
