class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def print_size(self):
        print("{} by {}".format(self.width, self.height))

class ShapeSquare(Shape):  # Create a child class of parent class "Shape".
    def area(self):
        return self.width * self.height

    def print_size(self):  # The method in child class has priority if same name method in parent class. Like an override.
        print("I am {} by {}.".format(self.width, self.height))

my_square = ShapeSquare(20, 25)
print(my_square.area())
my_square.print_size()
