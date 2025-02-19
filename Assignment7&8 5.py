import math
class Shape:
    def area(self):
        print("this method should be override by derived class")
    def perimeter(self):
        print("this method should be override by derived class")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"area of rectangle :{self.length * self.breadth}")
    def perimeter(self):
        print(f"perimeter of rectangle :{2 *(self.length + self.breadth)}")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"area of circle : { math.pi * self.radius **2}")
    def perimeter(self):
        print(f"perimeter of circle : {math.pi * 2 * self.radius}")
rect=Rectangle(4,3)
cir=Circle(5)
rect.area()
rect.perimeter()
cir.area()
cir.perimeter()
