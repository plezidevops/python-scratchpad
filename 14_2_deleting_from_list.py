# clear() removes everything from the list
grades = [90, 89, 87, 78, 94, 87]
grades.clear()
print(grades)

# you can do grades = [], but this creates a new list

# pop to remove individual item at the end of the list
grades = [90, 89, 87, 78, 94, 87]
grades.pop()
print(grades)

# pop() to remove item at a specific index in the list
item_removed = grades.pop(2)
print('item remove: ', item_removed)
print(grades)

# IndexError if no item exist
# grades.pop(9) #=> IndexError: pop index out of range

# remove() to remove the first value it finds
grades.remove(78)
print(grades)

# ValueError if value isn't there
# grades.remove(9) #=> ValueError: list.remove(x): x not in list


