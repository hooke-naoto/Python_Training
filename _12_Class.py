# Object-Oriented Programming

# class Orange:  # Object should be capitalized, no underscores. Orange, LikeThis, ...
#     def __init__(self):  # __ init__ is the special method to create objects. "self" is the object and registered automatically.
#         print("Created!")

class Orange:
    def __init__(self, w, c):  # Define variables for the object "Orange".
        self.weight = w  # Not defined data type here.
        self.color = c  # Not defined data type here.
        print("Created!")

    def public_method(self):  # Allow to use from exthernal (client).
        pass

    def _private_method(self):  # Not allowed to use from exthernal (client). Beginning from underscre "_". Just a rule in Python.
        pass

object = Orange(10, "dark orange")  # w = 10, c = "dark orange"
print(object)
# Created!
# <__main__.Orange instance at 0x10257db90>

print(object.weight)  # 10
print(object.color)  # "dark orange"

object.weight = 100
object.color = "light orange"

print(object.weight)  # 100
print(object.color)  # "light orange"

object1 = Orange(4, "light orange")
object2 = Orange(8, "dark orange")
object3 = Orange(14, 987)  # You can input any data type because it isn't defined in Class section.

print(object1.weight)
print(object1.color)
print(object2.weight)
print(object2.color)
print(object3.weight)
print(object3.color)
