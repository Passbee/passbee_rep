class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'bark bark'


class Cat(Animal):
    def talk(self):
        return 'meow meow'


def what_does_animal_says(animal):
    print(animal.talk())


cat = Cat()
dog = Dog()


what_does_animal_says(dog)
what_does_animal_says(cat)