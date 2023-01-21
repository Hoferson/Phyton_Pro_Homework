class Group_limit_error(Exception):

    def __init__ (self, message, limit):
        self.message = message
        self.limit = limit

    def __str__ (self):
        return f'{self.message}{self.limit}'

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

class Group:

    def __init__ (self, title, limit):
        self.title = title
        self.members = []
        self.limit = limit

    def add_member (self, member):
        if len(self.members) < self.limit:
            self.members.append(member)
        else:
            raise Group_limit_error('Group limit reached: ', self.limit)
        
    def remove_member (self, member):
        if member in self.members:
            self.members.remove(member)
            
    def search (self, surname):
        for i in self.members:
            if i.surname == surname:
                return i

    # def __str__ (self):
    #     return f"Group {self.title}\n {''.join(map(lambda item: str(item) ,self.members))}"  # здесь почему-то ''.join не работает с '\n'

    def __str__ (self):
        result = f"Group {self.title}\n"
        result += '\n'.join(map(lambda item: str(item) ,self.members))
        
        return result
    




student_1 = Student('Max', 'Maximov', 16)
student_2 = Student('Frank', 'Franko', 23)
student_3 = Student('Mark', 'Markov', 45)
student_4 = Student('kler', 'klerov', 12)
student_5 = Student('Rey', 'Reyov', 19)
student_6 = Student('Ronald', 'Ronaldov', 17)
student_7 = Student('Tery', 'Teryov', 16)
student_8 = Student('Goodvin', 'Goodvinenko', 18)
student_9 = Student('Lukas', 'Lukasefskiy', 22)
student_10 = Student('Robert', 'Robertino', 27)
student_11 = Student('Buratino', 'Wooden', 1)

teacher = Teacher('Danil', 'Danilov', 30)

group = Group('Python_Pro', 10)

try:
    group.add_member(teacher)
    group.add_member(student_1)
    group.add_member(student_2)
    group.add_member(student_3)
    group.add_member(student_4)
    group.add_member(student_5)
    group.add_member(student_6)
    group.add_member(student_7)
    group.add_member(student_8)
    group.add_member(student_9)
    group.add_member(student_10)
    group.add_member(student_11)

except Group_limit_error as error:
    print(error)



print(group)
print('\nsearch result: '+ str(group.search('Ronaldov')))

