class Descriptor:                                               # 4
    def __init__(self, item):
        self.item = item

    def  __get__(self, instance, cls):
        return self.item
    
    def __set__(self, instance, value):
        if self.item not in instance.__dict__:
            instance.__dict__[self.item] = value

        else:
            raise AttributeError('read-only')
            
    def __delete__(self, instance):
        raise AttributeError('cannot delete')
    

class Road:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    lenght = Descriptor('lenght')
    width = Descriptor('width')
    
    def __str__(self):
        return f'{road1.__dict__}'
    
road1 = Road(200, 40)
print(road1)
road1.lenght = 1
