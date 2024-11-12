import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2  # Compute radius from diameter
        elif radius is not None:
            self.radius = radius  # Given radius
        else:
            raise ValueError("Circle must have either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(r={self.radius:.2f}, d={self.diameter:.2f})"
    
    def __repr__(self):
        return f"Circle(r={self.radius:.2f}, d={self.diameter:.2f})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius # Add 2 circles together
            return Circle(radius=new_radius)
        elif isinstance(other, (int, float)):
            return Circle(radius=self.radius + other)  # Add integer or float to radius
        raise TypeError("Can only add Circle or numerical value.")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius  # Compare radius values of circles
        raise TypeError("Can only compare with another Circle.")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius  # Check if radius equal to another radius
        raise TypeError("Can only compare with another Circle.")

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        elif isinstance(other, (int, float)):
            self.radius += other
        else:
            raise TypeError("Can only add Circle or numerical value.")
        return self
# Example:
circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)
circle3 = Circle(radius=7)

print(circle1)
print(circle2)
print(circle3)

print(f"Area of circle1: {circle1.area():.2f}")
print(f"Area of circle2: {circle2.area():.2f}")

circle4 = circle1 + circle2
print(f"circle4 (circle1 + circle2): {circle4}")

circle5 = circle1 + 3
print(f"circle5 (circle1 + 3): {circle5}")

print(f"Is circle1 bigger than circle2? {circle1 > circle2}")  # False
print(f"Are circle1 and circle2 equal? {circle1 == circle2}")  # False

circle1 += circle3
print(f"circle1 after += circle3: {circle1}")

circle_list = [circle1, circle2, circle3, circle4, circle5]
sorted_circles = sorted(circle_list, key=lambda c: c.radius)

print("Sorted circles by radius:")
for c in sorted_circles:
    print(c)