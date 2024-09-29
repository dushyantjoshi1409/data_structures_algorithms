class math():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def __add__(self, other):
        return self.a + self.b + other.a + other.b
    def __mul__(self, other):
        temp_num = self.a * other.a
        temp_den = self.b * other.b
        return f"math({temp_num}/{temp_den})"

    def __str__(self, other):
        return f"math({self.a}, {self.b})"
x = math(2, 3)
print(x.add())
y = math(3, 4)
print(y.add())
print(x+y)
print(x*y)
