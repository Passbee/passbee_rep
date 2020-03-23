class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f'Hi, my name is {self.first_name} {self.last_name}, I\'m {self.age} years old.')


class Student(Person):
    def __init__(self, first_name, last_name, age, form):
        super().__init__(first_name, last_name, age)
        self.form = form

    def talk(self):
        print(f'Hi, my name is {self.first_name} {self.last_name}, I\'m {self.age} years old.\nI\'m {self.form}th '
              f'form student.')


class Teacher(Person):
    def __init__(self, first_name, last_name, age, study):
        super().__init__(first_name, last_name, age)
        self.study = study

    def talk(self):
        print(f'Hi, my name is {self.first_name} {self.last_name}, I\'m {self.age} years old.\nI teach {self.study} in school.')


if __name__ == '__main__':
    student = Student('Mike', 'Rossberg', '12', '7')
    student.talk()
    teacher = Teacher('Alfred', 'Malkovich', '45', 'Physics')
    teacher.talk()