class Shape:
    def __init__(self):
        pass    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


length=int(input(" length of the rectangle: "))
width=int(input("width of the rectangle: "))


r=Rectangle(length, width)

print("the area of the rectangle is", r.area())
