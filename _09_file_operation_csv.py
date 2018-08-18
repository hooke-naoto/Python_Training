# csv files
import csv  # import csv module!

list_123 = ["one", "two", "three"]
list_456 = ["four", "five", "six"]

with open("/Users/hooke/Documents/Coding/Python_Training/test3.csv", "w") as f:
    w = csv.writer(f, delimiter=",")  # You can use any delimiter (, ; / | ...).
    w.writerow(list_123)
    w.writerow(list_456)

with open("/Users/hooke/Documents/Coding/Python_Training/test3.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    # print(r)  # r is just a handle. <_csv.reader object at 0x10ffdfe50>
    for row in r:
        # print(row)
        print(",".join(row))
