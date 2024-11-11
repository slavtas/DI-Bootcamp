# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1) #prints diameter
# print(nc.diameter)

# nc.grow()
# print(nc.diameter)

# class Animal():
#     def __init__(self, number_legs, sound, type = None):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     def __init__(self,number_legs,sound,is_trained):
#         super().__init__(number_legs,sound)
#         self.is_trained = is_trained
#     def fetch_ball(self):
#         if self.is_trained:
#             print("I am a dog, and I love fetching balls")
#         else:
#             print('This dog is not trained!')

#     def barking(self):
#         super(Dog,self).make_sound()

# rex = Dog('dog', 4, "Wouaf")
# rex.make_sound()

# dog1 = Dog(4, 'Woof', True)

# rex.barking()

# class Door:
#     def __init__(self,is_opened):
#         self.is_opened = is_opened
#     def open_door(self):
#         if self.is_opened:
#             print('Door was open')
#         else:
#             print('Door is now opened')
            
#     def close_door(self):
#         if not self.is_opened:
#             print('Door is closed')
#         else:
#             self.is_opened = False

# class BlockedDoor(Door):
#     def open_door(self):
#         raise Exception('Blocked Door cannot be open')
#     def close_door(self):
#         raise Exception('Blocked Door cannot be closed')

# door1 = Door()
# door2 = BlockedDoor()

# door1.close_door()
# print(door1.is_opened)

# door2.close_door()

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

try:
    sum(my_list)
except:
    raise TypeError('There are strings in the list')