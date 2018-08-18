# Use os module to avoid troubles with file path.
import os
x = os.path.join("Users", "bob", "st.txt")
print(x)  # "Users/bob/st.txt"

# open()
# r: readable
# w: writable
# w+: writable & readble

st = open("/Users/hooke/Documents/Coding/Python_Training/test1.txt", "w")
st.write("Hi from Python!")
st.close()

# You can use "with" operator to omit closing operation.
# "with" close all files automatically.
with open("/Users/hooke/Documents/Coding/Python_Training/test2.txt", "w") as f:
    f.write("Hi from Python!")

# You can read text in txt file.
with open("/Users/hooke/Documents/Coding/Python_Training/test2.txt", "r") as f:
    x = f.read()
    print(x)

my_list = []
with open("/Users/hooke/Documents/Coding/Python_Training/test2.txt", "r") as f:
    my_list.append(f.read())
print(my_list)
