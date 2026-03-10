class Circle:
    
    def area(self, radius):
          area = 3.14 * radius * radius
          return area
    
    def perimeter(self, radius2):
          perimeter = radius2 * 3.14
          return perimeter

radius=int(input("Enter a radius: "))
radius2=radius*2
result = Circle().area(radius)
print(f"Area: {result}")
result2 = Circle().perimeter(radius2)
print(f"Perimeter: {result2}")

