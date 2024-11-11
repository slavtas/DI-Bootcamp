# Exercise_1 Cats' Breed
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siames(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# sara_pets = Pets([
#     Bengal('Puffy', 2),
#     Chartreux('Luffy', 4),
#     Siames('Muffy', 3)
# ])

# sara_pets.walk()

# === * === * === * === * === * === * === * === * === * === * === * === * ===

# Exercise_2 Dogs' Race
# class Dog:
#     def __init__(self,name,age,weight):
#       self.name = name
#       self.age = age
#       self.weight = weight

#     def bark(self):
#       return f'{self.name} is barking'
#     def run_speed(self):
#       return (self.weight/self.age)*10
#     def race(self,other_dog):
#         self_stamina = self.run_speed()*self.weight
#         other_dog_stamina = other_dog.run_speed()*other_dog.weight

#         if self_stamina > other_dog_stamina:
#           return f'{self.name} wins the race against {other_dog.name}!'
#         elif self_stamina < other_dog_stamina:
#           return f'{other_dog.name} wins the race against {self.name}!'
#         else:
#           return f'It\'s a tie for {self.name} and {other_dog.name}!'
        
# dog1 = Dog('Ponzo', 5, 25)
# dog2 = Dog('Spike', 7, 21)
# dog3 = Dog('Lessy', 4, 32)
# dog4 = Dog('Lucky', 6, 24)

# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())
# print(dog4.bark())

# print(f'{dog1.name} runs at {dog1.run_speed()} mph')
# print(f'{dog2.name} runs at {dog2.run_speed()} mph')
# print(f'{dog3.name} runs at {dog3.run_speed()} mph')
# print(f'{dog4.name} runs at {dog4.run_speed()} mph')

# print(dog1.race(dog2))
# print(dog2.race(dog3))
# print(dog3.race(dog4))
# print(dog4.race(dog1))

# === * === * === * === * === * === * === * === * === * === * === * === * ===

# Exercise_3 Dogs Doing Tricks
# from dog_class import Dog

# import random

# class PetDog(Dog):
#     def __init__(self,name,age,weight,trained=False):
#         super().__init__(name,age,weight)
#         self.trained = trained
    
#     def train(self):
#         print(self.bark())
#         self.trained = True

#     def play(self,*other_dogs):
#         all_dogs = [self.name]+[dog.name for dog in other_dogs]
#         print(f"{', '.join(all_dogs)} are playing all together")

#     def do_a_trick(self):
#         if self.trained:
#             tricks = [
#                 f'{self.name} does a barrel roll',
#                 f'{self.name} stands on back legs',
#                 f'{self.name} shakes your hand',
#                 f'{self.name} plays dead'
#             ]
#             print(random.choice(tricks))
#         else:
#             print(f'{self.name} needs training before doing any tricks')

# dog1 = Dog('Ponzo', 5, 25)
# dog2 = Dog('Spike', 7, 21)
# dog3 = Dog('Lessy', 4, 32)
# dog4 = Dog('Lucky', 6, 24)

# pet_dog = PetDog('Dingo', 3, 18)
# pet_dog.train()
# pet_dog.play(dog1,dog2,dog3,dog4)
# pet_dog.do_a_trick()

# === * === * === * === * === * === * === * === * === * === * === * === * ===

# Exercise_4 American Dad's Family Tree
# class Family:
#     def __init__(self, last_name, members=None):
#         self.last_name = last_name
#         self.members = members if members else []

#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Congratulations to the {self.last_name} family on the birth of {kwargs.get('name')}!")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] >= 18
        
#         raise ValueError(f"{name} is not in the family.") # returns Error message if not part of the Family

#     def family_presentation(self):
#         print(f"The {self.last_name} Family:")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

# family_members = [
#     {'name': 'Peter', 'age': 40, 'gender': 'Male', 'is_child': False},
#     {'name': 'Lois', 'age': 36, 'gender': 'Female', 'is_child': False}
# ]
# griffin_family = Family(last_name="Griffin", members=family_members)

# griffin_family.family_presentation()

# griffin_family.born(name='Stewie', age=0, gender='Male', is_child=True)

# print(griffin_family.is_18('Lois'))
# print(griffin_family.is_18('Stewie'))

# try:
#     print(griffin_family.is_18('Cleveland')) # Check if anyone else is part of the family
# except ValueError as error:
#     print(error)  # Output: Cleveland is not part of the family.

# griffin_family.family_presentation() # final check and presentation of family members

# === * === * === * === * === * === * === * === * === * === * === * === * ===

# Exercise_5
class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs.get('name')}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        raise ValueError(f"{name} is not in the family.")

    def family_presentation(self):
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses their power: {member['power']}!")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")
        else:
            raise ValueError(f"{name} is not in the family.")

    def incredible_presentation(self):
        print("*Here is our powerful family!*")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible Name: {member['incredible_name']}, Power: {member['power']}")

incredible_members = [
    {'name': 'Robert', 'age': 39, 'gender': 'Male', 'is_child': False, 'power': 'super strength', 'incredible_name': 'Mr. Incredible'},
    {'name': 'Helen', 'age': 36, 'gender': 'Female', 'is_child': False, 'power': 'stretching', 'incredible_name': 'Elastigirl'}
]

incredibles_family = TheIncredibles(last_name="Incredibles", members=incredible_members)

incredibles_family.incredible_presentation()

incredibles_family.born(name='Jack-Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

incredibles_family.incredible_presentation()