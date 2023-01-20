# Write a Python program that computes for the Area() and Perimeter() of a Rectangle
# Use the Shape as parent class
# Use Area() and Perimeter() as methods with its attributes length and width
# Use Rectangle as child class


class Shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def Area(self):
    return self.length * self.width

  def Perimeter(self):
    return (self.length + self.width)*2

class Rectangle(Shape):
    pass

rectangle = Shape(25,15)
rectangle2 = Shape(15, 10)

print("The Area is", rectangle.Area())
print("The Perimeter is",rectangle.Perimeter())

print("The Area for rectangle2 is",(rectangle2.Area()))
print("The Perimeter for rectangle2",(rectangle2.Area()))