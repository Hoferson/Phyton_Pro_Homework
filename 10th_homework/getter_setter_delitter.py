import time


class Road:                                                                     # 5 & 6
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def __str__(self):
        return f'lenght = {self.lenght} km, width = {self.width} m'
    
    def __setattr__(self,name, value):
        if type(value) == int:
            self.__dict__[name] = value

            with open('log.txt', 'a') as file:
                file.write(f'\n{time.ctime()} attribute {name} in instance of Road class, has been set/added, current value: {value}')

        else:
            raise ValueError('Value must be integer')
        
road1 = Road(200, 40)
print(road1)
road2 = Road(200.3, 40)