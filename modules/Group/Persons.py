class Person:

    def __init__ (self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__ (self):
        return f'{self.name} {self.surname} | age: {self.age}'

class Student(Person):

    def __init__ (self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__ (self):
        return f'Student: {Person.__str__(self)}'

class Teacher(Person):

    def __init__ (self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__ (self):
        return f'Teacher: {Person.__str__(self)}'