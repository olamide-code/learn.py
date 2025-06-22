#simple calculator
import math
operator = input("kindly choose an operator (+,-,/,*): \n")
num1 = int(input("enetr your first number \n"))
num2 = int(input("enetr your second number \n"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)
else:
    print("invalid operator")
    
#DETERMINE THE CIRCUMFERENCE OF A CIRCLE

radius = float(input("Enter the radius of the circle"))
circum = 2 * math.pi * radius
print(f"The circumference is: {round(circum, 2)}CM")

#DETERMINE THE AREA OF A CIRCLE IS
A = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(A,2)}cm^2")

#DETERTERMINE THE WEIGHT OF A BODY
weight = float(input("Enter your weight \n"))
unit = input("Kilograms or Pounds? (k or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"

elif unit == "L":
    weight = weight / 2.205
else:
    print(f"{unit} was not valid")

#DETERMINE DETAILS OF A PERSON
name = input("Enter your full name: \n")
N = len(name)
if N >= 5:
    print(N)
else:
    print("your name is too short")

