def average(*args):
    return sum(args) / len(args)

print(average(12, 34, 56, 78, 90))
print(average(12, 34, 56))
print(average(12, 34))
print(average(12))


grades = [89, 67, 78, 90, 87, 98]

# The * operator, when applied to an iterable argument in a function 
# call, unpacks its elements. 
print(average(*grades))