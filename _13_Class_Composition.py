# 2 different classes, but one has another's object.

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:  # The object "Person" will be a variable in Dog().
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)  # "mick" is an object, but also a variable as "owner" in Dog().
print(stan.owner.name)  # "stan.owner" is also an object in Person(), so you can describe further period and variable name.
