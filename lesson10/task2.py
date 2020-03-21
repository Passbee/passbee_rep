class DOG:
    def __init__(self, dog_age):
        self.age_factor = 7
        self.age = dog_age

    def human_age(self):
        print(self.age * self.age_factor)


if __name__ == '__main__':
    Rex = DOG(5)
    Rex.human_age()
