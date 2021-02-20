for item in "Python":
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1,2,3,4,5,6,7]:
    print(item)

#Range Function to count to 10 instantly
for item in range(10):
    print(item)

for item in range(5,10): #5,6,7,8,9,10
    print(item)

for item in range(5,10,2): # 5,7,9 with 2 as step
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    #total =  total + price
    total += price
print(f'Total: {total}')

######################################################

#Nested For Loops
#Coordinates for x, y
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

######################################################

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers_1 = [1,4,3,4,1]
for x_count in numbers_1:
    output = ''
    for count in range(x_count):
        output += 'l'
    print(output)

My attempt
for x in numbers:
    if x == 5:
        print('xxxxx')
    else:
        print('xx')

####################################################

#List
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[2]) # Mosh
print(names[-1]) # Mary
print(names[2:4]) # Mosh and Sarah
print(names[:]) # returns whole list

##################################################

#find the largest number in a list
list = [100, 200, 5, 4 , 950, 78]
#max method to find largest number
print("Largest number of the list is:", max(list))

numbers_2 = [3,6,2,8,4,10]
max = numbers_2[0]
for number in numbers_2:
    if number > max:
        max = number
print(max)

#####################################################

#2D List
matrix = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]

print(matrix[0][1]) # Answer 2
print(matrix[1][1]) # Answer 5
print(matrix[2][1]) # Answer 8

for row in matrix:
    for item in row:
        print(item)

################################

#List Methods
numbers_3 = [5,2,1,7,4]
numbers_3.pop() # 4 value is popped out of list
print(numbers_3)


numbers_3.append(15) # Add number at the end of list
print(numbers_3)

numbers_3.insert(0, 10)
print(numbers_3) # Add a number at the beginning of a list

# numbers_3.clear
# print(numbers_3)

#print(numbers_3.index(5)) # 1 index

print(50 in numbers_3) # False Boolean Value

print(numbers_3.count(5)) # Counts the occurence of value 5 in List is 1

numbers_3.sort()
print(numbers_3) # List is in ascending order

numbers_3.reverse()
print(numbers_3) # List is in descending order

numbers_4 = numbers_3.copy()
print(numbers_4) # Copy of the List numbers_3

# My attempt
# list(dict.fromkeys(numbers_3))
# print('The list is empty', numbers_3)

uniques = []
for number in numbers_3:
    if numbers_3 not in uniques:
        uniques.append(numbers_3)
print(uniques.append(numbers_3)) # No duplicates are found to list

####################################################################

#Tuple
number_5 = (1,2,3)
number_5[0] = 10
print(number_5[0])
