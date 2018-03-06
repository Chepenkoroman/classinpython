class Animal:
    name = None  # animal name
    animal_cry = None  # moo / baa / oink / quack / cluck / honk
    animal_class = None  # bird / mammal
    animal_type = None  # cow / goat / sheep / pig / chicken / duck / goose
    animal_cover = None  # feather / fur / skin

    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        print("Meet {})".format(self.name))

    def get_animal_class(self):
        print("{} is {}".format(self.name, self.animal_class))

    def get_animal_cover(self):
        print("{} is covered by {}".format(self.name, self.animal_cover))

    def get_animal_cry(self):
        print("{} says {}".format(self.name, self.animal_cry))

    def get_full_animal_description(self):
        print("Meet {}.".format(self.name))
        print("{} is {} and it is a {}.".format(self.name, self.animal_class, self.animal_type))
        print("It is covered by {}.".format(self.animal_cover))
        print("{} says '{}'.".format(self.name, self.animal_cry))

class Bird(Animal):
    animal_class = "bird"
    animal_cover = "feather"


class Mammal(Animal):
    animal_class = "mammal"
    animal_cover = "skin"

class Cow(Mammal):
    animal_type = "cow"
    animal_cry = "moo"

class Sheep(Mammal):
    animal_type = "sheep"
    animal_cry = "bee"

class Goat(Mammal):
    animal_type = "goat"
    animal_cry = "bee"

class Pig(Mammal):
    animal_type = "pig"
    animal_cry = "oink"

class Chicken(Bird):
    animal_type = "chicken"
    animal_cry = "cluck"

class Duck(Bird):
    animal_type = "duck"
    animal_cry = "quack"

class Goose(Bird):
    animal_type = "goose"
    animal_cry = "honk"
    
cow = Cow("Dorothy")
cow.get_full_animal_description()

print("\n=========\n")

duck = Duck("Peter")
duck.get_full_animal_description()
