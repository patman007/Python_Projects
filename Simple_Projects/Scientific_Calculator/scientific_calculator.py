# Import math module/library
import math

#Operations in scientific calculator
#Defined Add Function with parameters
def add (a,b):
    return a + b

#Defined Subtract Function with parameters
def subtract(a,b):
    return a - b

#Defined Multiplication Function with parameters
def multiply(a,b):
    return a * b

#Defined Division Function with parameters
def divide(a,b):
    return a / b

#Defined Square Root Function with parameter
def sqrt(a):
    result =  math.sqrt(a)
    return result

#Defined Exponents Function with parameter
def exp(a):
    return a ** 2

#Defined Sin() Function with parameter
def sin(x):
    result = math.six(x)
    return result

#Defined Cos() Function with parameter
def cos(x):
    result = math.cos(x)
    return result

#Defined Tan() Function with parameter
def tan(x):
    result =  math.tan(x)
    return result

#Choosing an operation to use for user input
print("""
    1 - Addition (x,y)
    2 - Subtraction (x,y)
    3 - Multiplication (x,y)
    4 - Divide (x,y)
    5 - Square(x)
    6 - Square root(x)
    7 - sin(x)
    8 - cos(x)
    9 - tan(x)""")
#op variable is user input for calculator
op = int(input('What operation do you want to perform? '))

#Calculator script
#WHILE LOOP with IF STATEMENTS for op user input
while op < 10:
    #1 Addition
    if op == 1:
        print('Enter the parameters: ')
        x1 = int(input('Enter x: '))
        y1 = int(input('Enter y: '))
        res1 = add(x1, y1)
        print('Addition= ', res1)

    #2 Subtraction
    elif op == 2:
        x2 = int(input('Enter x: '))
        y2 = int(input('Enter y: '))
        res2 = subtract(x2, y2)
        print('Subtraction= ', res2)

    #3 Multiplication
    elif op == 3:
        x3 = int(input('Enter x: '))
        y3 = int(input('Enter y: '))
        res3 = multiply(x3, y3)
        print('Multiplication= ', res3)

    #4 Division
    elif op == 4:
        x4 = int(input('Enter x: '))
        y4 = int(input('Enter y: '))
        res4 = divide(x4, y4)
        print('Division= ', res4)

    #5 Squareroot
    elif op == 5:
        x5 = int(input('Enter x: '))
        res5 =  sqrt(x5)
        print('Squareroot= ', res5)

    #6 Exponents
    elif op == 6:
        x6 = int(input('Enter x: '))
        res6 = exp(x6)
        print('Exponents= ', res6)

    #7 Sin(x)
    elif op == 7:
        x7 = int(input('Enter x: '))
        res7 = sin(x7)
        print('Sin(x)= ', res7)

    #8 Cos(x)
    elif op == 8:
        x8 = int(input('Enter x: '))
        res8 = cos(x8)
        print('Cos(x)= ', res8)

    #9 Tan(x)
    elif op == 9:
        x9 = int(input('Enter x: '))
        res9 = tan(x9)
        print('Tan(x)= ', res9)

    #ELSE Statement
    else:
        print('Choose another operation ')

    #new variable to continue the scientific calculator or BREAK the program
    new = int(input('Do you want to continue - (YES - 1), (NO - 0): '))

    #IF STATEMENT for 1 YES or 0 NO
    if new == 1:
        op = int(input('Enter an operation: '))
    #Breaks out of the loop
    elif new == 0:
        print('Thanks for using the scientific calculator')
        break
