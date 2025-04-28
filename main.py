# Ethan Lawrnce
# April 28 2025
# Python Classes

class Dog:
    """ A simple dog """
    # Methods
    def __init__(self, name, age):
        '''init statement'''
        self.name = name
        self.age = age
    # End of Init
    def sit(self):
        print(f'{self.name}, is now sitting')
    def roll_over(self):
        print(f'**{self.name} rolls over**')
    def description(self):
        print(f'{self.name} is a {self.age} year old, dog!')

my_dog = Dog('Jack', 7)
your_dog = Dog('Muffin', 3)

dogs = []
dogs.append(my_dog)
dogs.append(your_dog)

for dog in dogs:
    print()
    dog.sit()
    dog.roll_over()
    dog.description()
    dog.age += 1
    dog.description()
    print()