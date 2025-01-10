import math

# Greetings function
def greetings(name):
    name = input("What is your name?")
    print(f"Hello  {name} !!")

#Area formula function
def square_area():
    try:
        length = float(input("Give the length of the side of the square: "))
        area = length * length
        print(f"The square area is :{area}")
    except ValueError:  
        print("Error. Enter a valid value")
        
def rectangle_area():
    try: 
        length = float(input("Give the length of the rectangle: "))
        width = float(input("Give the width of the rectangle: "))
        area =  length * width 
        print(f"The area of the rectangle is : {area}")
    except ValueError:
        print("Error. Enter valid values")  

def triangle_area():
    try:
        base = float(input("Give the base of the triangle: "))
        height = float(input("Give the height of the triangle: "))
        area = (base * height) / 2
        print(f"The area of the triangle is: {area}")
    except ValueError:
        print("Error. Enter valid values")

def circle_area():
    try:
        radius = float(input("Give the radius of the circle: "))
        area = math.pi * radius * radius
        print(f"The area of the circle is :{area}")
    except ValueError:
        print("Error. Enter a valid value")

def trapezoïd_area ():
    try:
        small_base = float(input("Give the small base of the trapezoïd: "))
        big_base = float(input("Give the big base of the trapezoïd: "))
        height = float(input("Give the height of the trapezoïd: "))
        area = ((small_base + big_base) * height ) / 2
        print(f"The area of the trapezoïd is :{area}")
    except ValueError:
        print("Error. Enter valid values")

def main():
    try:
        #Geometric area calculation
        print(" --- Geometric figures surface --- ")
        format = input("Give the format of the figure (rectangle/square/triangle/circle/trapezoïd): ")

        #Build a short meny that will match the area formula with the form of the figure.
        match format.lower():
            case "square":
                square_area()

            case "rectangle":
                rectangle_area()
            
            case "triangle":
                triangle_area()

            case "circle":
                circle_area()

            case "trapezoïd":
                trapezoïd_area()
    except  Exception as e:
        print(f"Une erreur s'est produite : {e}")
        print("Enter a valid choice.")

#Checking if a number is even/odd - perfect - primeNumber

def even_odd(number):
    if number%2 == 0:
        return True
    if number%2 != 0:
        return False

def prime_number(number):
    divider = 0
    for i in range(2, number):
        if (divider > 1):
            return False
            break
        elif number % i == 0 :
            divider += 1
    if (divider == 1):
        return True

def perfect_number(number):
    divider_sum = 1
    for i in range(2,number):
        if number % i == 0:
            divider_sum += i
    if divider_sum == number:
        return True
    else:
        return False


if __name__  == "__main__":
    main()
