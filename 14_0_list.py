# Creating a list
my_list = [1, 2, 3, 4]
print(my_list)

my_list = list('pascal')
print(my_list)

my_empty_list = []
print(my_empty_list)

my_other_empty_list = list()
print(my_other_empty_list)

# List methods
number = [1, 3, 4, 2, 3, 1, 5, 2]
print(number.count(1))
print(number.index(2))

# reverse the list in-place
number.reverse()
print(number)

# Add to a list
# append to the end of the list
students = ['paul', 'jude', 'pascal']
students.append('mamie')
print(students)

# insert at specific position in the list
students.insert(0, 'baby')
students.insert(len(students), 'jean')
print(students)

# extends to add an iterable to a list
grades = [90, 89, 87, 78, 94, 87]
students.extend(grades)
print(students)

a_list = []

for number in range(1, 6):
    a_list += [number]