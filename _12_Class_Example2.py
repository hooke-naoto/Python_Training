class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):  # Return the area, effective after both width and length are defined.
        return self.width * self.length

    def change_size(self, w, l):  # Can change both width and length of existed object.
        self.width = w
        self.length = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
# 200
# rectangle = Rectangle(20, 40)
rectangle.change_size(20, 40)
print(rectangle.area())
# 800
