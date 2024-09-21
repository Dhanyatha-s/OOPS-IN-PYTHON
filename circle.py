class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        print((22/7) * self.radius **2)

    def Perimeter(self):
        print(2 *(22/7) * self.radius )



c1 = Circle(21)
c1.Area()
c1.Perimeter()