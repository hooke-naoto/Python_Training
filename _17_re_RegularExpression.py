import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)
# matches = re.findall("beautiful", l, re.IGNORECASE)  # If you want to search without sensitive (uppercase/lowercase).

print(matches)
