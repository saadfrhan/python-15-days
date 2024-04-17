import math

radius = float(input("Enter radius in degrees: "))

circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(f"Circumference: {round(circumference, 2)}")
print(f"Area: {round(area, 2)}")
