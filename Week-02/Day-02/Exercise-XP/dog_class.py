class Dog:
    def __init__(self,name,age,weight):
      self.name = name
      self.age = age
      self.weight = weight

    def bark(self):
      return f'{self.name} is barking'
    def run_speed(self):
      return (self.weight/self.age)*10
    def race(self,other_dog):
        self_stamina = self.run_speed()*self.weight
        other_dog_stamina = other_dog.run_speed()*other_dog.weight

        if self_stamina > other_dog_stamina:
          return f'{self.name} wins the race against {other_dog.name}!'
        elif self_stamina < other_dog_stamina:
          return f'{other_dog.name} wins the race against {self.name}!'
        else:
          return f'It\'s a tie for {self.name} and {other_dog.name}!'
        
dog1 = Dog('Ponzo', 5, 25)
dog2 = Dog('Spike', 7, 21)
dog3 = Dog('Lessy', 4, 32)
dog4 = Dog('Lucky', 6, 24)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(dog4.bark())

print(f'{dog1.name} runs at {dog1.run_speed()} mph')
print(f'{dog2.name} runs at {dog2.run_speed()} mph')
print(f'{dog3.name} runs at {dog3.run_speed()} mph')
print(f'{dog4.name} runs at {dog4.run_speed()} mph')

print(dog1.race(dog2))
print(dog2.race(dog3))
print(dog3.race(dog4))
print(dog4.race(dog1))