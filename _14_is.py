# "is" use for check same or not.

class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)
# True (same)

another_bob = Person()
print(bob is another_bob)
# False (not same)
# Not same because "bob" and "another_bob" are created separately by Person().



# "is" is good for checking of None data also.

x = 10
if x is None:
    print("x is None.")
else:
    print("x is not None.")

x = None
if x is None:
    print("x is None.")
else:
    print("x is not None.")
