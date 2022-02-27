'''
When a function receives as an argument a reference 
to an immutable (unmodifiable) object—such as an int, 
float, string or tuple—even though you have direct access
 to the original object in the caller, you cannot modify 
 the original immutable object’s value.
'''

x = 7

def cube(number):
    print('id(number) before modifying number:', id(number))
    number **= 3
    print('id(number) after modifying number:', id(number))
    return number

cube(x)
print(f'x = {x}; id(x) = {id(x)}')