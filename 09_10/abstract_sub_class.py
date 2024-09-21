from abstract_class import Shape


# sub class1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# sub class2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    # # 사용 예시
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")

    print(f"Circle area: {circle.area()}")
    print(f"Circle perimeter: {circle.perimeter()}")
