# Exercise_1 Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat('Sally', 8)
cat_2 = Cat('Tom', 5)
cat_3 = Cat('Bandit', 13)

cats = [cat_1, cat_2, cat_3]

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats[1:]:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cats)   

print(f'The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old')

# -------------------------------------------------

# Exercise_2 Dogs
class Dog:
    def __init__(self,dog_name,dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        return f'{self.name} goes woof!'

    def jump(self):
        return f'{self.name} jumps {self.height*2} cm high!'
    
davids_dog = Dog('Rex', 50)
print(f'David\'s dog name is {davids_dog.name} and it is {davids_dog.height} cm high.', davids_dog.bark(), davids_dog.jump())

sarahs_dog = Dog('Teacup', 20)
print(f'Sarah\'s dog name is {sarahs_dog.name} and it is {sarahs_dog.height} cm high.', sarahs_dog.bark(), sarahs_dog.jump())

if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is bigger')
elif sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is bigger')
else:
    print(f'Both {davids_dog.name} and {sarahs_dog.name} are the same height')

# -------------------------------------------------

# Exercise_3 Karaoke
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

all_star = Song(['Somebody once told me','The world is gonna roll me','I ain\'t the sharpest tool in the shed','She was looking kind of dumb','With her finger and her thumb','In the shape of an "L" on her forehead'])

all_star.sing_me_a_song()

# -------------------------------------------------

# Exercise_4 'Madagascar' Deleted Scenes
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f'{new_animal} has been added to the zoo.')
        else:
            print(f'{new_animal} is already in the zoo.')
    
    def get_animals(self):  # Changed to plural "get_animals"
        print('Animals at the Zoo:', self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)  # Corrected to self.animals
            print(f'{animal_sold} has been sold.')
        else:
            print(f'{animal_sold} is not in the zoo.')
    
    def sort_animals(self):
        animals_by_letter = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in animals_by_letter:
                animals_by_letter[first_letter].append(animal)
            else:
                animals_by_letter[first_letter] = [animal]
        
        self.grouped_animals = {}
        for group_number, (letter, animals) in enumerate(animals_by_letter.items(), start=1):
            self.grouped_animals[group_number] = animals[0] if len(animals) == 1 else animals

    def get_groups(self):
        print("Animal groups in the zoo:")
        for group, animals in self.grouped_animals.items():
            print(f"{group}: {animals}")


# Example Usage
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Giraffe")

# Displaying animals
ramat_gan_safari.get_animals()

# Selling an animal
ramat_gan_safari.sell_animal("Baboon")
ramat_gan_safari.get_animals()

# Sorting and displaying groups of animals
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()