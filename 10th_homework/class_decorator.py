class_register = []                                         #1

def class_register_decorator(cls):
    def registrator(*args, **kwargs):
        instance = cls(*args, **kwargs)
        class_register.append(cls)
        return instance
    return registrator

@class_register_decorator
class Road:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def __str__(self):
        return f'lenght = {self.lenght} km, width = {self.width} m'
    
road = Road(100, 40)
print(road)
print(class_register)

print('\n')

# class add_string_to_class:                                #2 Я так і не зрорзумів як створити класс-декоратор, 
#     def __init__(self, cls, string):                          який буде приймати 1 додатковий єлемент.
#         self.cls = cls
#         self.string = string

#     def __call__(self, *args, **kwargs):
#         instance = self.cls(*args, **kwargs)
#         return instance
    
#     def __str__(self):
#         return f'{self.string} {cls.__str__()}'


# @add_string_to_class('m240')
# class Road200:

#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width

#     def __str__(self):
#         return f'lenght = {self.lenght} km, width = {self.width} m'
    
# road200 = Road200(100,40)
# print(road200)
# print(road200.string)

class Box:                                                  #3
    def __init__(self, lenght, width, height):
        self.lenght = lenght
        self.width = width
        self.height = height

    def sum_volume(box1, box2):
        return box1.height * box1.lenght * box1.width + box2.height * box2.lenght * box2.width

    
    def __str__(self):
        return f'Box\nlenght: {self.lenght}\nwidth: {self.width}\nheight: {self.height}'
    
box1 = Box(10, 20, 30)
box2 = Box(10, 20, 100)
print(Box.sum_volume(box1, box2))