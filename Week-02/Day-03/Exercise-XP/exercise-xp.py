# Exercise_1 USD and NIS
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         currency_name = self.currency if self.amount == 1 else self.currency + "s"
#         return f"{self.amount} {currency_name}"
    
#     def __repr__(self):
#        return str(self)
    
#     def __int__(self):
#         return self.amount
    
#     def __add__(self, other):
#         if isinstance(other, Currency) and self.currency == other.currency:
#             return Currency(self.currency, self.amount + other.amount) #congrats! currencies match
        
#         elif isinstance(other, int):
#             return Currency(self.currency, self.amount + other) #integer recognized as native to currency
        
#         else:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>") #currencies don't match
        
#     def __iadd__(self, other):        
#         if isinstance(other, Currency) and self.currency == other.currency:
#             self.amount += other.amount
#         elif isinstance(other, int):
#             self.amount += other
#         else:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

#         return self

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_2 Import
from func import sum_numbers

sum_numbers(5,3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_3 String Module
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

print(generate_random_string())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_4 Current Date
import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()

print(f"Today is {today_date.strftime('%d/%m/%Y')}, {actual_datetime.strftime('%H:%M')}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_5 Time Left Till January 1st
from datetime import datetime

def time_until_new_year():
    next_year = datetime(datetime.now().year + 1, 1, 1)
    time_left = next_year - datetime.now()
    
    print(f"Time left until New Year: {time_left.days} days, {time_left.seconds // 3600} hours, {(time_left.seconds % 3600) // 60} minutes, and {time_left.seconds % 60} seconds")

time_until_new_year()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_6 Birthday and Minutes
from datetime import datetime

def minutes_lived(birthdate_str):
    
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

    now = datetime.now()
    
    delta = now - birthdate
    
    minutes = delta.total_seconds() / 60
    
    print(f"You have lived {int(minutes):,} minutes.")

# Example usage:
birthdate = "21/03/1985"  # Input in format DD/MM/YYYY
minutes_lived(birthdate)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise_7 Faker
# import faker

# fake = faker()

# users = []

# def add_user():
#     user = {
#         "name": fake.name(),
#         "address": fake.address(),
#         "language_code": fake.language_code()
#     }
#     users.append(user)

# for _ in range(5):
#     add_user()

# for user in users:
#     print(user)

