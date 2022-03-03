grades = [90, 89, 87, 78, 94, 87]

# sort(), sorts the grades in-place, meaning the grades-list will be modified
grades.sort()
print(grades)

# reserve the sorted list
grades.sort(reverse=True)
print(grades)

# sorted() creates a new list and original list remains intact
students = ['paul', 'jude', 'pascal', 'anes']
new_student_list = sorted(students)
print(f'id(students: {id(students)} : {students}')
print(f'id(new_student_list: {id(new_student_list)} : {new_student_list}')