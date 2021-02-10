#Unpackaging
#coordinates in this example is a tuple
coordinates = (1,2,3)
# x =  coordinates[0]
# y = coordiantes[1]
# z = coordiantes[2]

#Unpackaging is a short hand to do this on Line 8
x,y,z = coordinates
print('Unpackaging coordinates:', x, y, z)

################################################

#Dictionaries uses key value pairs
customer= {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) # John Smith the key value names are case Sentsive in dictionaries
print(customer.get("name")) # John Smith
print(customer.get('birthdate')) # None
print(customer.get('birthdate', 'Jan 1 1980')) # Jan 1 1980 is a default value put in place instead of None

#Replace a key value pair in dictionary
customer['name'] = 'Jack Smith'
print(customer["name"]) # Jack Smith

#Add a new key value pair in dictionary
customer['birthdate'] = 'Jan 1 1980'
print(customer['birthdate']) # Jan 1 1980

#Customer dictionary
print(customer) # {'name': 'Jack Smith','age': 30, 'is_verified': True, 'birthdate': 'Jan 1 1980'}

######################################################################################################

phone = (input('Enter four numbers: '))
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

###################################################

#Functions
def greet_user():
    print('Hi there!')
    print('Welcome aboard')

print("start")
greet_user()
print('Finish')

#####################################################

#Parameters
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')

print("start")
# Arguments
greet_user("John")
greet_user('Mary')
print('Finish')

################################################

#Parameters
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("start")

# Positional Arguments
#use for string arguments more than numerical if possible
greet_user("John", "Smith")


#Keyword arguments should be used for numerical arguement readab
#total=50, shipping=5, percent=0.1

# Keyword Arguements and should always come after positional arguments
greet_user("John", last_name='Mason')

print('Finish')

########################################################################

def square(number):
    return number * number

# result = square(3)
# print(result)
print(square(3))

##############################################################################

#Try prevents the program from crashing such as showing ValueError mesasge
#Try
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
#You can have many exceptions depending on the program you are doing
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

#############################################################################

#Classes
#Pascal Naming convention means capitalize first letter of the class name
class Point:
    #Defined function
    def move(self):
        print('move')

    #Defined function
    def draw(self):
        print('draw')

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x) # 10
print(point1.y) # 20
point1.draw() # draw


point2 = Point()
point2.x = 1
print(point2.x) # 1

###############################################################################


#Constructors
#Pascal Naming convention means capitalize first letter of the Class name
class Point:
    #Defined function
    # Constructor "__int__"
    def __init__(self, x , y):
        self.x = x
        self.y = y


    #Defined function
    def move(self):
        print('move')

    #Defined function
    def draw(self):
        print('draw')

point = Point(10, 20)
print(point.x)

#########################################################################

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person("John Smith")
john.talk()
# print(john.name) # John Smith
# john.talk() # talk

bob = Person('Bob Smith')
bob.talk()

#########################################################################

#Inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog (Mammal):
    #pass
    def bark(self):
        print('bark')


class Cat(Mammal):
    #pass
    def meow(self):
        print('meow')


dog1 = Dog()
dog1.bark()
dog1.walk()

cat1 = Cat()
cat1.meow()
cat1.walk()
