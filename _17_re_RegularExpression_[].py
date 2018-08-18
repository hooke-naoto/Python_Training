import re

string = "Two too."
m = re.findall("t[wo]o", string, re.IGNORECASE)  # search the words which include any letters in [].
print(m)

m = re.findall("t[mnopqr]o", string, re.IGNORECASE)
print(m)
