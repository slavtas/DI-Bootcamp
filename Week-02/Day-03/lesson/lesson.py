# import collections

# dictionary1 = { 'a' : 1, 'b' : 2 }  
# dictionary2 = { 'c' : 3, 'b' : 4 }  
# chain_Map = collections.ChainMap(dictionary1, dictionary2)  
# print(chain_Map.maps) 

# from collections import OrderedDict  
# order = OrderedDict()  
# order['a'] = 1  
# order['b'] = 2  
# order['c'] = 3  
# print(order)  

# #unordered dictionary
# unordered=dict()
# unordered['a'] = 1  
# unordered['b'] = 2  
# unordered['c'] = 3 
# print("Default dictionary", unordered)

# iterate over three lists
# import itertools

# list_one = ['a', 'b', 'c']
# list_two =['d', 'e', 'f']
# list_three = ['1', '2', '3']

# result = itertools.chain(list_one, list_two, list_three)

# for element in result:
#   print (element)

# import itertools

# my_list = [0, 0, 1, 2, 0]

# result = itertools.dropwhile(lambda x: x == 0, my_list)

# for elements in result:
#   print (elements)

# class Dog():
#     dogs_king = "Bernie IV"

#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print(f"{self.name} barks ! WAF")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def rename(self, new_name):
#         self.name = new_name

# my_dog = Dog("Rex")
# my_dog.rename("Paul")
# print(my_dog.name)

# class Dog():
#     number_of_dogs = 0
#     dogs_king = "Bernie IV"

#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog
#         # Increment the number of dogs
#         Dog.number_of_dogs += 1

#     def bark(self):
#         print(f"{self.name} barks ! WAF")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def rename(self, new_name):
#         self.name = new_name

# my_dog = Dog("Rex")
# my_dog2 = Dog("Bernie V")
# print(f"Curently, there are {Dog.number_of_dogs} dogs")

# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# class MyClass:
#   @staticmethod
#   def add(a, b): 
#     return a + b

# print(MyClass.add(3, 6))

# class MyClass:
#   __counter = 0

#   @classmethod
#   def add(cls,a): 
#     return cls.__counter + a

# my_class_add = MyClass.add(3)
# print(my_class_add)

# new_class = MyClass()
# new_class.__counter = 1

# print(new_class.add(3))

# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.__first_name = first_name
#     self.__last_name = last_name

#   @property
#   def email(self): 
#     return f"{self.__first_name}.{self.__last_name}@gmail.com"

#   @email.setter
#   def email(self, full_name):
#     name, last_name = full_name 
#     self.__first_name = name
#     self.__last_name = last_name

# newClass = MyClass("John", "Doe")
# newClass.email = ("Sarah","Parker")
# print(newClass.email)

# class Person:

#     used_names = set()

#     def __init__(self, name, age):
#         if name in self.used_names:
#             name = input("That name is taken. Enter another name: ")

#         self.name = name
#         self.age = age
#         self.used_names.add(name)

#     @classmethod
#     def fromYear(cls, name, birth_year):
#         THIS_YEAR = 2020
#         return cls(name, THIS_YEAR - birth_year)

#     @property
#     def professional_name(self):
#         return "Mr " + self.name

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1

#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value


# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)

# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

# class Person:
#     def __init__(self, name, lname, age):
#         self.name = name
#         self.lname = lname
#         self.age = age

#     def __call__(self):
#         print (f"Person: {self.name} {self.lname}, Age: {self.age}")

# person1 = Person("Sarah J.","Parker", 25)
# person1()
# person3 = Person('Bobby', 'Singer', 56)
# person3()

# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age  = age

#   def __repr__(self):
#       return f"{self.__class__.__name__} : {self.name} {self.age}"

# newPerson = Person('Sarah', 24)

# print(newPerson)

# class Person:
#   def __init__(self, name, lastName):
#       self.name = name
#       self.lastName = lastName

#   def __repr__(self):
#       return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#   def __add__(self, other):
#       return Person(self.name, other.lastName)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)

# print(type(dragonChild))

# print(dir(dragonChild))

# first_list = ["a", "b", "c"]
# second_list = ["d", "e", "f"]

# print("\nCalling the `+` builtin with both lists")
# print(first_list + second_list)
# # >> Calling the `+` builtin with both lists
# # ['a', 'b', 'c', 'd', 'e', 'f']

# print("\nCalling `__add__()` with both lists")
# print(first_list.__add__(second_list))

# class Person:
#   def __init__(self, name, lastName):
#       self.name = name
#       self.lastName = lastName

# #Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

#   def __repr__(self):

# # We can write whatever we want inside this method, but we have to return an object.

#       return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#   def __add__(self,other):
#       name = self.name[0] + other.name[1:]
#       lastname = other.lastName
#       return Person(name,lastname)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)

# import sys
# import typing

# from tabulate import tabulate

# def main(file1, file2):
#     file1_contents = extract_file_contents(file1)
#     file2_contents = extract_file_contents(file2)

#     display_files(file1_contents, file2_contents)

#     dates = sorted(set(file1_contents).union(file2_contents))
#     print(dates[len(dates) // 2])

# def display_files(file1_contents, file2_contents):
#     table = {
#         'file1': file1_contents,
#         'file2': file2_contents
#     }
#     print(tabulate(table))

# def extract_file_contents(file_path: str) -> typing.List[str]:
#     """ 
#     Extract file contents and strip whitespaces from each row.
#     : param file_path: The path to the file to extract
#     : return: A list of date data rows
#     """ 

#     with open(file_path, 'r') as f:
#         file_contents = f.readlines()
#     new_file_contents = []
#     for date_data_record in file_contents:
#         date_data_record = date_data_record.strip()
#         if date_data_record:
#             new_file_contents.append(date_data_record)
#     return new_file_contents

# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if len(args) != 2:
#         print(f"Expected two arguments as files. Got {len(args)} instead.")
#         sys.exit(1)
#     main(*args)

# import os

# def create_structure(base_dir, weeks=5,days=5):
#     for week in range(1, weeks + 1):
#         week_dir = os.path.join(base_dir, f"week{week}")
#         os.makedirs(week_dir, exist_ok=True)

#         for day in range(1, days + 1):
#             day_dir = os.path.join(week_dir, f"day{day}")
#             os.makedirs(day_dir, exist_ok=True)

#             for subfolder in ['lesson','homework']:
#                 os.makedirs(os.path.join(day_dir, subfolder), exist_ok=True)

#     print("Directory structure was created successfully")

# base_directory = 'courses'

# create_structure(base_directory)

# import time

# before = time.time()
# long_number = 1000**1000
# after = time.time()

# print (f'It took {after-before} seconds to execute 1000**1000')
# import datetime

# today_date = datetime.date.today()
# actual_datetime = datetime.datetime.now()
# in_20_hours = actual_datetime + datetime.timedelta(hours=20, minutes=34)

# print(f"Today is {today_date.strftime('%d/%m/%Y')}, {actual_datetime.strftime('%H:%M')}")
# print(f"In 20 hours and 34 minutes it will be {in_20_hours.strftime('%d/%m/%Y, %H:%M')}")

# import datetime

# birth_date = datetime.datetime(1985, 3, 21)  

# now = datetime.datetime.now()

# current_year = now.year
# next_birthday = datetime.datetime(current_year, birth_date.month, birth_date.day)

# time_until_birthday = next_birthday - now

# days = time_until_birthday.days
# hours, remainder = divmod(time_until_birthday.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# # Print the countdown
# print(f"My birthday is in {days} days, and {hours:02}:{minutes:02}:{seconds:02}")

