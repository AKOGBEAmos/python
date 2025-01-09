import math

# Greetings function
def greetings(name):
    name = input("What is your name?")
    print(f"Hello  {name} !!")

#Geometric area calculation
print(" --- Geometric figures surface --- ")
format = input("Give the format of the figure (rectangle/square/triangle/circle/trapezoïd): ")

#Build a short meny that will match the area formula with the form of the figure.
match format:
    case "square":
        def rectangle_area(length):
            length = int(input("Give the length of the side of the square: "))
            area = pow(length,2)
            print(f"The square area is :{area}")
    case "rectangle":
        def square_area(length, width):
            length = int(input("Give the length of the rectangle: "))
            width = int(input("Give the width of the rectangle: "))
            area =  length * width 
            print(f"The area of the rectangle is : {area}")
    
    case "triangle":
        def triangle_area(base,height):
            base = int(input("Give the base of the triangle: "))
            height = int(input("Give the height of the triangle: "))
            area = (base * height) / 2
            print(f"The area of the triangle is: {area}")

    case "circle":
        def circle_area(radius):
            radius = int(input("Give the radius of the circle: "))
            area = math.pi * pow(radius, 2)
            print(f"The area of the circle is :{area}")

    # case "trapezoïd":
    #   def trapezoïd_area (small_base, big_base, height):
    #       small_base = int(input("Give the small base of the trapezo: "))
                        