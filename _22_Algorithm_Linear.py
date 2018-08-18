# Linear Algorithm
# Keep to try in order till the answer.

def ss(number_list, n):
    found = False  # False at initial.
    for i in number_list:
        if i == n:
            found = True  # True if you get number "n" in "number_list".
            break
    return found  # False if you didn't get number "n" in "number_list".

numbers = range(0, 100)  # Input a list of numbers from 0 to 99. [0, 1, 2, ... 99]
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)
