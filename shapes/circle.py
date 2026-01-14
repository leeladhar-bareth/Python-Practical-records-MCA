from .point import Point

class Circle:
    def __init__(self, radius, center_x=0, center_y=0):
        self.radius = radius
        self.center = Point(center_x, center_y)

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius