## Without exception handling:
# Program crashes and shows ugly error message
#ATM Machines
#Common errors in Python:
'''Dividing by zero,Open afile that doesnot exist,wrong input example needs an name and we enter int'''
'''Jab aapke code mein error aaye aur aap ne khud koi plan nahi banaya us error ke liye — to Python ka apna system woh error pakad kar screen par message dikhata hai aur program band kar deta hai.'''
def divide(a, b):
    result = a / b
    return result

x = divide(5, 0)
print(x)
#Check for valid input first
def divide(a,b):
    if b == 0:
        result = 'Error: cannot divide by zero'
        return result
    else:
        result = a/b
        return result
x = divide(5,0)
print(x)
#hat if “b” is not a number?
def divide(a,b):
    if (type(b) is not int and type(b) is not float):
        result = 'Error:divisor is not a number'
        return result
    elif b == 0:
        result = "Error: Cannot divide by zero"
        return result
x = divide(5,0)
print(x)

