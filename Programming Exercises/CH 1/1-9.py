from logging import exception


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise RuntimeError("Numbers passed into Fraction class must be integers.")
        else:
            cmmn = gcd(abs(top), abs(bottom))
            
            if bottom < 0:
                top *= -1
                bottom *= -1
                
            self.num = top // cmmn
            self.den = bottom // cmmn

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)
    
    def __repr__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num
    
    def __ne__(self, other_fraction):
        return not (self == other_fraction)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __radd__(self, other_fraction):
        return self + other_fraction
    
    def __iadd__(self, other_fraction):
        self = self + other_fraction

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __lt__(self, other_fraction):
        return self.num / self.den < other_fraction.num / other_fraction.den

    def __le__(self, other_fraction):
        return self.num / self.den <= other_fraction.num / other_fraction.den

    def __gt__(self, other_fraction):
        return self.num / self.den > other_fraction.num / other_fraction.den

    def __ge__(self, other_fraction):
        return self.num / self.den >= other_fraction.num / other_fraction.den

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))
        
    def get_num(self): return self.num
    
    def get_den(self): return self.den

x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
print(y - x)
print(x * y)
print(x / y)
print(x < y)
print(x > y)