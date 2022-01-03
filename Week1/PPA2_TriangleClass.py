import math

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        if((self.a + self.b) > self.c and
            (self.b + self.c) > self.a and
            (self.c + self.a) > self.b):
            return 'Valid'
        else:
            return 'Invalid'
    
    def Side_Classification(self):
        if(self.is_valid() == 'Invalid'):
            return 'Invalid'
        else:
            if(self.a == self.b == self.c):
                return 'Equilateral'
            elif(self.a == self.b or self.b == self.c or self.c == self.a):
                return 'Isosceles'
            else:
                return 'Scalene'
    
    def Angle_Classification(self):
        if(self.is_valid() == 'Invalid'):
            return 'Invalid'
        else:
            if((self.a * self.a) + (self.b * self.b) == (self.c * self.c)):
                return 'Right'
            elif((self.a * self.a) + (self.b * self.b) > (self.c * self.c)):
                return 'Acute'
            else:
                return 'Obtuse'
    
    def Area(self):
        if(self.is_valid() == 'Invalid'):
            return 'Invalid'
        else:
            s = (self.a + self.b + self.c) / 2
            return(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)))