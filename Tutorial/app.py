print('Subscribe now') # string
print('Patrick Mason') # string

print('o----o') #string
print(' ||||') #string

print('*' * 10) #string

###################################

#Integers
price = 10 #cariable in Python
price = 20 #variable updated in Python
rating = 4.9 #variable updated in Python
name = 'Mosh'
is_publicshed = False #Boolean True or False
print(price)

full_name = 'John Smith'
age = 20
is_new = True
print(full_name,age, is_new)

######################################

name = input('What is your name? ')
color = input('What is your favorite color? ')
print('Hi '  + name + ' likes ' + color)


#####################################

birth_year = input('Birth year: ') # or int(input('Birth year: '))
print(type(birth_year))
age = 2021 - int(birth_year) # or 2021 - int(birth_year)
print(type(age))
print(age)
int()
float()
bool()

########################################

weight_pounds = float(input('What is your weight: '))
print(type(weight_pounds))
weight_kg = weight_pounds * 0.45
print(type(weight_kg))
print(weight_kg)

##########################################

course = "Python's for Beginners"
# or course = 'Python for "Beginners"'
print(course)

#''' is multi line strings
course_1 = '''
Hi John
Here is our first email to you.

Thank you,
The support team
'''
print(course_1)

#Index of first character and last character
course_2 = 'Python for Beginners'
print('This is the first character: ', course_2[0]) #first character
print('This is the last character: ', course_2[-1]) # last character
print('Thes are the characters: ', course_2[0:3]) # zero index to second index, third index is cutoff point
print('Thes are the characters: ', course_2[1:]) #lists every index except the zero index


# Copies of first variable [:]
course_2 = 'Python for Beginners'
another = course_2[:]
print(another)

# [1:-1] will show all indexes except first and last
name = 'Jennifer'
print(name[1:-1]) # ennife


#################################################################################

#John [Smith] is a coder
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
#Formatted String same as temperate literals
msg = f'{first} [{last}] is a coder'
print(msg)

#len for counting the number of characters including spaces
course = 'Python for Beginners'
print(len(course))
#len and print are general purpose function unlike a method
#for numbers, objects, or strings, etc.

#Title method
print(course.)


#Dot operator
#Upper Case methoed
print(course.upper())
#Lower Case method
print(course.lower())

#Find index method and is sensitive to uppercase and lowercase characters
print(course.find('y'))
print(course.find('o')) # this finds the first o only
print(course.find('O')) # this finds the first O only, but none are found which equals -1

#Replace Method
print(course.replace('Beginners', 'People')) # replace entire word
print(course.replace('P', 'J')) # replace one letter Jython for Beginners

#in operator show a Boolean expression of True or False
# checking to see if Python string is in variable course
print('Python' in course) # True
print('python' in course) # False








