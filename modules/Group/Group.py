import Exceptions
import Persons

class Group:

    def __init__ (self, title, limit):
        self.title = title
        self.members = []
        self.limit = limit

    def add_member (self, member):
        if len(self.members) < self.limit:
            self.members.append(member)
        else:
            raise Exceptions.Group_limit_error('Error: group limit reached: ', self.limit)
        
    def remove_member (self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            raise Exceptions.Member_doesnt_exist(f'{member} is not in this group')
            
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
    




student_1 = Persons.Student('Max', 'Maximov', 16)
student_2 = Persons.Student('Frank', 'Franko', 23)
student_3 = Persons.Student('Mark', 'Markov', 45)
student_4 = Persons.Student('kler', 'klerov', 12)
student_5 = Persons.Student('Rey', 'Reyov', 19)
student_6 = Persons.Student('Ronald', 'Ronaldov', 17)
student_7 = Persons.Student('Tery', 'Teryov', 16)
student_8 = Persons.Student('Goodvin', 'Goodvinenko', 18)
student_9 = Persons.Student('Lukas', 'Lukasefskiy', 22)
student_10 = Persons.Student('Robert', 'Robertino', 27)
student_11 = Persons.Student('Buratino', 'Wooden', 1)

teacher = Persons.Teacher('Danil', 'Danilov', 30)

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

except Exceptions.Group_limit_error as error:
    with open('log.txt', 'w') as file:
        file.write('\n'+str(error))
    print(error)

except Exceptions.Member_doesnt_exist as error_2:
    with open('log.txt', 'w') as file:
        file.write('\n'+str(error_2))
    print(error_2)



print(group)
print('\nsearch result: '+ str(group.search('Ronaldov')))

