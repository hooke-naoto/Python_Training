class Orange:
    def __init__(self, w, c):
        """weight is gram"""
        self.weight = w
        self.color = c
        self.mold = 0  # Add a "class bariable" (mold), it's different "instance variables" (weight, color).
        print("Created!")

    def rot(self, days, temp):
        """temperature is degree-C"""
        self.mold = days * temp  # Method (object).rot has been created, and it rewrite Variable "(object).mold".

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)
# Created!
# 0
# 370
