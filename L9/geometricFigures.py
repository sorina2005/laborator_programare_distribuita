import math

# 1. Clasa de Bază
class Shape:
    def area(self):
        """
        Aceasta este o metodă 'abstractă' în concept.
        Clasele copil vor trebui să o definească pe a lor.
        """
        pass

# 2. Clasa Copil - Cerc
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculăm aria specifică cercului: π * r^2
        return math.pi * (self.radius ** 2)

    def __str__(self):
        # Dunder method pentru afișare.
        # Apelăm self.area() direct în string pentru a afișa rezultatul calculat.
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

# 3. Clasa Copil - Dreptunghi
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Calculăm aria specifică dreptunghiului: L * l
        return self.width * self.height

    def __str__(self):
        # Dunder method pentru afișare.
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

# --- ZONA DE TESTARE ---

# Instanțiere
circle = Circle(5)
rectangle = Rectangle(10, 4)

# Afișare directă (aici intră în acțiune __str__)
print(circle)
print(rectangle)

# Demonstratrea Polimorfismului
print("-" * 30)
print("Demonstrație Polimorfism (Listă de forme):")

shapes = [circle, rectangle]

for shape in shapes:
    # Aici este polimorfismul: apelăm .area() pe elementul 'shape',
    # fără să ne pese dacă este Cerc sau Dreptunghi.
    # Python știe ce metodă să apeleze în funcție de obiect.
    print(f"Aria formei este: {shape.area():.2f}")