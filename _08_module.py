import math  # import "math" module
a = math.pow(2, 3)  # math.pow() is the module of "math".
print(a)

import random
b = random.randint(0, 100)  # select random integer number from 0 to 100.
print(b)

import statistics
nums = [1, 5, 33, 12, 46, 33, 2]
c1 = statistics.mean(nums)
c2 = statistics.median(nums)
c3 = statistics.mode(nums)
print(c1)
print(c2)
print(c3)

import keyword  # check it is reserved words for Python or notself.
d1 = keyword.iskeyword("for")
d2 = keyword.iskeyword("football")
print(d1)
print(d2)

# Call your original module which is described other python files.
import _08_module_hello  # import "module_hello.py" from same directory (folder).
_08_module_hello.print_hello()  # call the module "print_hello()".

# All code run if you import other python files.
import _08_module_something
