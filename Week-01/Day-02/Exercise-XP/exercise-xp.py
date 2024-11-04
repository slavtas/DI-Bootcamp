# Exercise_1 Favorite Numbers
my_fav_numbers = {5, 7, 18, 42, 72, 69}

my_fav_numbers.add(13)
my_fav_numbers.add(44)
print(my_fav_numbers)

my_fav_numbers.remove(69)

friend_fav_numbers = {8, 4, 16, 32, 64, 3}

# Concatenate both sets by union
our_fav_numbers = my_fav_numbers | friend_fav_numbers

print("My Favorite Numbers:", my_fav_numbers)
print("Friend's Favorite Numbers:", friend_fav_numbers)
print("Our Favorite Numbers:", our_fav_numbers)

# Exercise_2 Tuple
# Tuples in Python are immutable, and their contents cannot be changed once they are created. But it's possible to create new tuple via combining the original with additional integers.
# e.g.
my_tuple = (1,2,3,4) #original tuple
print(my_tuple)
my_tuple = my_tuple + (5,6) #adding more integers via new tuple 'my_tuple + (5,6)
print(my_tuple)

# Exercise_3 List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

apple_count = basket.count("Apples")
print(f"Number of apples in the basket: {apple_count}")

basket.clear()
print(basket)

# Exercise_4 Floats
# integers are whole numbers, floats are numbers with decimal places
float_sequence = [round(1.5 + 0.5 * i, 1) for i in range(8)]
print(float_sequence)

# Exercise_5 for Loop
for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Exercise_6 while Loop
target_name = 'Slava' #True value

while True:
    user_name = input('Please enter your name: ')
    if user_name == target_name:
        print('Well done! You have fulfilled your destiny!')
        break  # Exit the loop
    else:
        print('You shall not pass! Unless you get the name right...')

# Exercise_7 Fav Fruits
favorite_fruits = input('Enter your favorite fruits, separated by a space: ')

favorite_fruits_list = favorite_fruits.split()
print(favorite_fruits_list)

chosen_fruit = input('Enter your favorite fruit: ')

if chosen_fruit in favorite_fruits_list:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy.')

# Exercise_8 Pizza Order
toppings = []

base_price = 10
topping_price = 2.5

while True:
    topping = input('Enter what you want to see on your pizza (or type "quit" to finish): ')

    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f'Adding {topping} to your pizza!')

total_price = base_price + (topping_price * len(toppings))
print('\nYour pizza toppings:')

for topping in toppings:
    print(f'- {topping}')

print(f'Total price: {total_price:.2f} USD')

# Exercise_9 Cinemax
# Family cost
total_cost = 0

family_size = int(input('How many people in the family need tickets? '))

for i in range(family_size):
    age = int(input(f'Enter the age of person {i+1}: '))
    
    
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price

print(f'The total cost for the family\'s tickets is: {total_cost} USD')

#Teenagers Admition
teenagers = ['Harry', 'Hermione', 'Ron', 'Rick', 'Morty']

for name in teenagers[:]:
    age = int(input(f'Enter the age of {name}: '))
        
    if 16 <= age <= 21:
        print(f'{name} is not permitted to watch the movie.')
        teenagers.remove(name)
    else:
        print(f'{name} is allowed to watch the movie.')

print('\nThe final list of teenagers allowed to watch the movie:')
print(teenagers)

# Exercise_10 Sandwich Crysis
# Initial list of sandwich orders
sandwich_orders = ['Tuna sandwich','Pastrami sandwich','Avocado sandwich','Pastrami sandwich','Egg sandwich','Chicken sandwich','Pastrami sandwich']

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f'I made your {current_sandwich}.')

print('\nAll sandwiches made:')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')


