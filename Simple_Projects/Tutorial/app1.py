# Arithmetic
print(10 + 3) # Addition
print(10 -3) # Subtraction
print(10 * 3) # Multiplication
print(10 **3) # Exponent 10 ^ 3 = 1000
print('Floating: ', 10 / 3) # Division for floating numbers /
print('Integer: ', 10 // 3) # Division for integer numbers  //
print(10 % 3) # Modulus Remainder from division

# Augmented assigned Operator
# Increment a number example
x = 10
x = x + 3 # or x += 3 answer is 13
x = x -3 # or x -= 3 answer is 7
print(x)

# Operator precedence
x =  10 + 3 * 2 #Answer 16
x = (10 + 3) * 2 #Answer 26
x = 10 + 3 * 2 ** 2 #Answer 22
x = (2 + 3) * 10 - 3 #Answer 47
print(x)

############################################


# Math function
x = 2.9
# Round function
print(round(x)) # Answer 3
# Absolute function
print(abs(-x)) # Answer 2.9

###########################################

## Rememeber to import Math module for complex calculations
# math module is an object or a string by doing this
import math
#Ceiling of a number
print(math.ceil(2.9)) # Answer 3
print(math.floor(2.9)) # Answer 2

#####################################################

# #If and else statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a coldy day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price  = 1000000
credit_good = False
if credit_good:
    print(f'Good credit at {price} is 10%')
    downpayment = price * .10
    print(f"Downpayment is: ${downpayment}")
else:
    print(f'No good credit at {price} is 20%')
    downpayment = price * .20
    print(f"Downpayment is: ${downpayment}")

###############################################################

#Remember Shift + Tab command to start at the beginning of the line
has_high_income =  True
has_good_credit =  True
has_criminal_record = False

#AND Operator
if has_high_income and has_good_credit:
    print('Eligible for loan')
#OR Operator
if has_high_income or has_good_credit:
    print('Eligible for loan now')
#NOT Operator
if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")

###################################################################

temperature = int(input('Enter temperature in Celsius: '))

if temperature > 30 or temperature == 30:
    print(f"It's a hot day at {temperature} Celsius")
elif temperature < 10 or temperature == 10:
    print(f"It's a cold day at {temperature} Celsius")
else:
    print(f"It's neither hot or cold at {temperature} Celsius")

# ################################################################

name = input('Enter a name: ')

if len(name) < 3:
    print('Name must be at least 3 characters long. Please enter another name')
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long. Please enter a another name")
else:
    print(f"{name} looks good")

# #####################################################################################

weight = float(input('Enter your weight: '))
unit_type= input(('Enter L for Pounds bs or K for Kilograms: '))

if (unit_type.upper() == 'L'):
    converted = weight * 0.45
    print(f'You are {converted} kilogram')
elif (unit_type.upper() =='K'):
    converted = weight / 0.45
    print(f'You are {converted} pounds')
else:
    print('Enter either Pounds ( l or L) or Kilogram ( k or K) ')

##############################################################################

#While Loops
i =  1
while i <= 5:
    print(i)
    i = i + 1
print("done")


j =  1
while j <= 5:
    print('*' * j)
    j = j + 1
print("done")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failed!')

#########################################

#While Loop with if-elif-else statements
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Car started...')
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command =="help":
        print("""
star - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command =="quit":
        break
    else:
        print("Sorry, I don't understand that")









