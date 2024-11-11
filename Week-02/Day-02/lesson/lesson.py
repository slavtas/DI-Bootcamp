# Multilevel Inheritance
# class Grandpa:
#     def speak(self):
#         print('Grandpa is speaking')
#     def sleep(self):
#         print('Grandpa is sleeping')

# class Parent(Grandpa):
#     def speak(self):
#         print('Parent is speaking')

# class Child(Parent):
#     pass

# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj2.sleep()

#  Multiple Inheritance

class Grandpa:
    def speak(self):
        print('Grandpa is speaking')
    def sleep(self):
        print('Grandpa is sleeping')

class Parent1(Grandpa):
    def speak(self):
        print('Parent is speaking')

    def eat(self):
        print('Parent1 is eating')

class Parent2(Grandpa):
    def speak(self):
        print('Parent2 is speaking')

class Child(Parent2, Parent1):
    pass

obj2 = Child()
obj2.sleep()