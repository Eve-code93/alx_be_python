import math

class Shape:
    """A base class representing a geometric shape."""

    def area(self):
        """Method to calculate the area of the shape. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
