import math

class Rational:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)
        if isinstance(other, int | float):
            return Rational(self.b * other + self.a, self.b)
    
    def __radd__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)
        if isinstance(other, int | float):
            return Rational(self.b * other + self.a, self.b)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)
        if isinstance(other, int | float):
            return Rational(self.b * other - self.a, self.b)
        
    def __rsub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)
        if isinstance(other, int | float):
            return Rational(self.b * other - self.a, self.b)
        
    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a*other.b, self.b*other.a)
        if isinstance(other, int | float):
            return Rational(self.a, self.b * other)
        
    def __rtruediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a*other.b, self.b*other.a)
        if isinstance(other, int | float):
            return Rational(self.a, self.b * other)
        
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a*other.a, self.b*other.b)
        if isinstance(other, int):
            return Rational(self.a * other, self.b)
        
    def __rmul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a*other.a, self.b*other.b)
        if isinstance(other, int | float):
            return Rational(self.a * other, self.b)
        
    def __str__(self):
        if self.a == self.b:
            return f'\n1'
        
        if math.gcd(self.a, self.b) > 1:
            self.resa = int(self.a/math.gcd(self.a, self.b))
            self.resb = int(self.b/math.gcd(self.a, self.b))
            if self.resa > self.resb:
                return f'\n{int(self.resa/self.resb)} {self.resa-int(self.resa/self.resb)*self.resb}/{self.resb}'
            if self.resa < self.resb:
                return f'\n{self.resa}/{self.resb}'
        
        if math.gcd(self.a, self.b) == 1:
            if self.a > self.b:
                return f'\n{int(self.a/self.b)} {self.a-int(self.a/self.b)*self.b}/{self.b}'
            if self.a < self.b:
                return f'\n{self.a}/{self.b}'

        
    
q = Rational(2, 5)
w = Rational(1, 2)
print(q)
print(w)
print(q*w)


    
