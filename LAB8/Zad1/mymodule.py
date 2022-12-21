from Triangle import triangle_area
from Rectangle import rectangular_area
from Square import square_area
from Rhombus import rhombus_area
from Trapezoid import  trapezoid_area

shape = input("Select shape: rectangle, square, rhombus, trapezoid, triangle - ")

if shape == "triangle":
    a = float(input("Enter side a: "))
    h = float(input("Enter height h: "))
    triangle_area(a, h)

elif shape == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    rectangular_area(a, b)

elif shape == "square":
    a = float(input("Enter side: "))
    square_area(a)

elif shape == "rhombus":
    a = float(input("Enter side a: "))
    h = float(input("Enter height h: "))
    rhombus_area(a, h)

elif shape == "trapezoid":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    h = float(input("Enter height h: "))
    trapezoid_area(a, b, h)

else:
    print("Wrong shape, please try again!")