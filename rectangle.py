
# Creating a class named Rectangle
class Rectangle:

    # Constructor to initialize length and breadth
    def __init__(self, length, breadth):
        self.length = length       # Assigning length to the object
        self.breadth = breadth     # Assigning breadth to the object

    # Method to calculate the area of rectangle
    def area(self):
        return self.length * self.breadth

    # Method to calculate the perimeter of rectangle
    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Creating two objects of Rectangle class
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Displaying the details of Rectangle 1
print("\nRectangle 1")
print("Area =", r1.area())
print("Perimeter =", r1.perimeter())

# Comparing the areas of two rectangles
if r1.area() > r2.area():
    print("\nRectangle 1 has greater area")

elif r1.area() < r2.area():
    print("\nRectangle 2 has greater area")

else:
    print("Both rectangles are equal")