class Hexagon:
    def __init__(self, l1, l2, l3, l4, l5, l6):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.length4 = l4
        self.length5 = l5
        self.length6 = l6

    def cal_perimeter(self):
        return self.length1 + self.length2 + self.length3 + self.length4 + self.length5 + self.length6

h = Hexagon(1, 2, 4, 7, 4, 1)
print(h.cal_perimeter(  ))
