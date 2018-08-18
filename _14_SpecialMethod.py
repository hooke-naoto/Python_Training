# print() performs for various data type, you can modify its function with override (special methods).




# print(object) calls object handle information normally, but you can override with __repr__.

# NORMAL
class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)
# <__main__.Lion instance at 0x108a13d40>

# SPECIAL
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)
# Dilbert




# print(calculation)

# NORMAL
x = -20
y = 10
print(x + y)

# SPECIAL
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
# 10
# = abs( -20 + 10 )
