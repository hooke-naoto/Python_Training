import re

line = "I love $"
m = re.findall("$", line, re.IGNORECASE)
print(m)
# (nothing)

line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)
# ['$'] can be found.
