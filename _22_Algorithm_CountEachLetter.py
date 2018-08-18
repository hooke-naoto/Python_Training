# Count each letter in a word.

def count_letter(string):
    count_dict = {}
    for c in string:
        if c.lower() in count_dict:
            count_dict[c.lower()] += 1
        else:
            count_dict[c.lower()] = 1

    print(count_dict)

count_letter("Dynasty")

print("\n")

# You can make it more easy with embeded module "collections" as followingself.
from collections import defaultdict
def count_letter(string):
    count_dict = defaultdict(int)
    # print(defaultdict(int))
    for c in string:
        count_dict[c] += 1
    print(count_dict)
    # print(count_dict["a"])
count_letter("Dynasty")

print("\n")

# You can make it more easy as followingself.
from collections import Counter
print(Counter("Dynasty"))
