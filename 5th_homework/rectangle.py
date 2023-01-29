class Rectangle:
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid

    def get_area(self,):
        return self.len * self.wid
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()
    def __gt__(self, other):
        return self.get_area() > other.get_area()
    def __le__(self, other):
        return self.get_area() <= other.get_area()
    def __ge__(self, other):
        return self.get_area() >= other.get_area()
    def __eq__(self, other):
        return self.get_area() == other.get_area()
    def __ne__(self, other):
        return self.et_area() != other.get_area() 
    
    def __add__(self, other):
        return Rectangle(self.len + other.len/2, self.wid + other.wid/2)
    def __radd__(self, other):
        return Rectangle(self.len + other.len/2, self.wid + other.wid/2)
    
    def __iadd__(self, other):
        self.len += other.len/2
        self.wid += other.wid/2
        return self
    
    def __mul__(self, other):
        return Rectangle(self.len * other, self.wid)
    def __rmul__(self, other):
        return Rectangle(self.len * other, self.wid)
    
    def __imul__(self, other):
        self.len *= other
        return self

    
    def __str__(self):
        return f'\nRectungle:\nlenght: {self.len}\nwidth: {self.wid}\narea: {self.get_area()}'
    

a = Rectangle(2, 3)
b = Rectangle(3, 4)
print(a)
print(b)
print(a+b)
print(3*a)


