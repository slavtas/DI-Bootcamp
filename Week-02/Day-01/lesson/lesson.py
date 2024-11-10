class Dog():
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
    
    def bark(self):
        print(f'{self.name} is barking')
    
    def walk(self,num_meters):
        return f'{self.name} walked {num_meters} meters today'
    
    def rename(self,new_name):
        self.name = new_name
        return self.name

shelter_dog = Dog('Rex', 'black', 7)
puddle = Dog('Fluffy', 'white', 3)

# Dog.bark(puddle)
# puddle.bark()

Dog.walk(puddle, 200)

# print(puddle.walk(200))
# print(shelter_dog.walk(500))

# puddle.rename('Bob')
# print(puddle.name)
# shelter_dog.bark()
# puddle.bark()

# # print(type(shelter_dog))
# # shelter_dog.name = 'Rex' #option 1 to create attribute to object
# # print(shelter_dog.name)



# print(puddle.name)
# print(shelter_dog.name)

# class Person():
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def presentation(self):
#         print(f'Hello, my name is {myself.name} and I am {myself.age} years old')





# myself = Person('Slava', 39, 1.71)
# print(myself.name, myself.age, myself.height)

# myself.presentation()
# myself.age +=1
# print(myself.age)

# print(myself.__dict__)

#exercises Computer

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# # Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")
