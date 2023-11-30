class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print( 3.14 * self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print( self.width * self.height)


# Creating instances of subclasses
circle = Circle(5)
circle.area()
rectangle = Rectangle(4, 6)
rectangle.area()



