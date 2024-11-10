class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self,animal_name, quantity=1):
        if animal_name in self.animals:
            self.animals[animal_name] += quantity
        else:
            self.animals[animal_name] = quantity

    def get_info(self):
        output = f'{self.name}\'s farm\n\n'
        for animal, quantity in self.animals.items():
            output += f'{animal} : {quantity}\n'
            output += '\nE-I-E-I-O!\n\n'
        return output
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_list = [f'{animal}s' if self.animals[animal] > 1 else animal for animal in self.get_animal_types()]
        animal_str = ', '.join(animal_list[:-1])+ ' and '+ animal_list[-1] if len(animal_list) > 1 else animal_list[0]
        return f'{self.name}\'s farm has {animal_str}'
    
macdonald = Farm("McDonald")

macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())