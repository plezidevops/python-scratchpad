students = [['paul', 'jude'], ['pascal', 'anes'], ['paulette', 'maurice']]

# copy() creates a shallow copy
new_students = students.copy()
print(new_students)

new_students[0][0] = 'Marlin'

print(students)
print(new_students)

# Deep copy
import copy

new_students_2 = copy.deepcopy(new_students)
new_students_2[0][0] = 'tipizo'
print(new_students_2)
print(new_students)