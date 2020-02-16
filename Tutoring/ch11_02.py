class Shape:
    def __init__(self,color="yellow",filled=True):
        self.color = color
        self.filled = filled
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def calcArea(self):
        return 3.14*(self.radius**2)

c = Circle(10)
print(c.color,c.filled,c.radius)