class PERSON:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.name} {self.last_name} and I’m {self.age} years old')


if __name__ == '__main__':
    person = PERSON('Carl', 'Johnson', '26')
    person.talk()
