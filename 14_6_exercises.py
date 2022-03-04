# 1. How do you create a list?
list1 = []
list2 = list()
list3 = [1,2,3]

# 2. Create a list with 3 items and then use append() to add two more. 
item_list = [1, 2, 3, 4]
item_list.append(6)

# 3. What is wrong with this code?
    # my_list=[1,2,3] 
    # my_list.remove(4)
# ValueError exception since 4 isn't in the list

# 4. How do you remove the 2nd item in this list?
my_list=[1,2,3]
my_list.pop(1)
print(my_list)

# 5. Create a list that looks like this: [4, 10, 2, 1, 23]. 
# Use string slicing to get only the middle 3 items.
my_list = [4, 10, 2, 1, 23]
item = my_list[2:3]
print(item)