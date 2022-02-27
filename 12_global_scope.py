# x has global scope
# can be used anywhere
x = 7

def access_global():
    ''' Accessing a global variable'''
    print('x printed from access_global: ', x)

access_global()

'''
by default, you cannot modify a global variable 
in a function—when you first assign a value to a variable 
in a function’s block, Python creates a new local variable:
'''

def try_to_modify_global():
    '''Try modifying a global variable'''
    x = 3.4
    print('x printed from try_to_modify_global: ', x) #=> 3.4

try_to_modify_global()
print(x) #=> 7

'''
To modify a global variable in a function’s block, 
you must use a global statement to declare that the 
variable is defined in the global scope:
'''

def modify_global():
    '''Modify the global variable scope'''
    global x
    x = 'hello'
    print('x printed from try_to_modify_global: ', x)

print(50 * '-')
print('x = ', x)
modify_global()
print('x = ', x)