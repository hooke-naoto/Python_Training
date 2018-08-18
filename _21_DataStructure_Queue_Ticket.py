# Simulation how many people can buy tickets with condition of 2 values.
a = 30  # Limit time for this simulation.
b = 1  # Max time for every customer. (Define each time as random less than this max value.)

import time  # embeded module, can show time[sec] as real number.
import random

class Queue:  # Object "Queue()"
    def __init__(self):  # Define object "Queue()" without variables.
        self.items = []  # Define a list "items" for object "Queue()".

    def is_empty(self):  # Check "items" is empty or not.
        return self.items == []

    def enqueue(self, item):  # Insert a item at the beginning of "items".
        self.items.insert(0, item)

    def dequeue(self):  # Cut a item at the end of "items".
        return self.items.pop()

    def size(self):  # Size of "items".
        return len(self.items)

    def simulate_line(self, till_show, max_time):  # Function "simulate_line()", "till_show"is time[sec] as integer, "max_time" is
        pq = Queue()
        tix_sold = []  # A list of members who got tickets.

        for i in range(100):  # Loop from 0 to 9.
            # pq.enqueue("person" + str(i))
            pq.enqueue("person{:0=3}".format(i + 1))  # "person001" ~ "person100"
            # print(str(i))
        # print(pq.items)
        # ['person9', 'person8', 'person7', 'person6', 'person5', 'person4', 'person3', 'person2', 'person1', 'person0']

        time_1st = time.time()
        time_end = time.time() + till_show
        print("time_1st: " + str(time_1st))
        print("time_end: " + str(time_end))

        time_now = time.time()
        while time_now < time_end and not pq.is_empty():  # Normally "now < t_end", and items is not yet empty.
            # r = random.randint(0, max_time)  # calculate the time each customer spent at ticket counter.
            r = random.random() * max_time  # calculate the time each customer spent at ticket counter.
            time.sleep(r)  # Wait for r[sec] which were created by random.random().
            person = pq.dequeue()
            tix_sold.append(person)  # Add each item every time.
            time_now = time.time()
            print(person + ": {:.2f}".format(r) + ", {:.3f}".format(time_now))

        # return tix_sold
        return "Last customer: \"" + person + "\" within " + str(till_show) + "[sec]."

queue = Queue()
sold = queue.simulate_line(a, b)  # till_show = 10, max_time = 5
print(sold)
