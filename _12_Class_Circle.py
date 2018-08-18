import math  # to use "pi".

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pow(self.radius, 2) * math.pi

    def change_radius(self, r):
        self.radius = r

circle = Circle(5)
print(circle.area())

circle.change_radius(1)
print(circle.area())
