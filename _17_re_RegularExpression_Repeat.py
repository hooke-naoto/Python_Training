import re

t = "__one__ __two__ __three__"
found = re.findall("__.*__", t)  # ".*" find longest word.
for match in found:
    print(match)
# __one__ __two__ __three__

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)  # ".*?" can find short word.
for match in found:
    print(match)
# __one__
# __two__
# __three__
