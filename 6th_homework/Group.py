class GroupIterator:

    def __init__(self, members):
        self.members = members
        self.index = 0

    def __next__(self):
        if self.index < len(self.members):
            self.index += 1
            return self.members[self.index-1]
        raise StopIteration

class Group_limit_error(Exception):

    def __init__ (self, message, limit):
        self.message = message
        self.limit = limit

    def __str__ (self):
        return f'{self.message}{self.limit}'
    
class Member_doesnt_exist(Exception):

    def __init__ (self, message):
        self.message = message
    
    def __str__ (self):
        return f'{self.message}'


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

    def __getitem__(self, index):
        if isinstance (index, int):
            if index < len(self.members):
                return self.members[index]
            raise IndexError()
        
        if isinstance(index, slice):
            start = index.start or 0
            stop = index.stop or len(self.members) - 1
            step = index.step or 1
            return list(map(str, self.members[start:stop:step]))
        
        raise TypeError()
    
    def __iter__(self):
        return GroupIterator(self.members)
        
    
    def __len__ (self):
        return len(self.members)

    def add_member (self, member):
        if len(self.members) < self.limit:
            self.members.append(member)
        else:
            raise Group_limit_error('Error: group limit reached: ', self.limit)
        
    def remove_member (self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            raise Member_doesnt_exist(f'{member} is not in this group')
            
    def search (self, surname):
        for i in self.members:
            if i.surname == surname:
                return i

    
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
    with open('log.txt', 'w') as file:
        file.write('\n'+str(error))
    print(error)

except Member_doesnt_exist as error_2:
    with open('log.txt', 'w') as file:
        file.write('\n'+str(error_2))
    print(error_2)

print(len(group))
print(group[1])
print(group[0:4:1])

for i in group:
    print(i)


