class Circle():
    # constructor
    def __init__(self,r):
        self.r =r
    def diameter(self):
        d = self.r*2
        print(d)

circle = Circle(5)
print(circle.r)
circle.diameter()