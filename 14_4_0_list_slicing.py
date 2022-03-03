# slice[start:end]

# the ability to get a little piece of the list
students = ['paul', 'jude', 'pascal', 'anes', 'paulette', 'maurice']

# I want pascal, anes, paulette
pap_list = students[2:5]
print(pap_list)  # => ['pascal', 'anes', 'paulette']

# last items in the list
slice2 = students[-1:]
print(slice2)  # => ['maurice']

# last 3 items: starts len(students)-3 upto to the last item
slice3 = students[-3:]
print('--> ', slice3)  # => ['anes', 'paulette', 'maurice']

# first 3 items: starts at index 0 upto not including 3
slice3 = students[:3]
print(slice3)  # => ['paul', 'jude', 'pascal']

# Reverse the list
slice4 = students[::-1]
print(slice4)
