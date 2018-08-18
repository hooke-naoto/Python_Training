class Rectangle:

    recs = []  # This is the class variable which is defined outside of __init__.

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))  # It adds data every running of __init__.

    def print_size(self):
        print("{} by {}".format(self.width, self.lenght))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)
# [(10, 24), (20, 40), (100, 200)] <- all values were added on class variable.
# Class variable can be used on several objects (r1, r2, r3) without global variables.
# Be careful to handle class barible because it has risk as same as global variables.
