## Without exception handling:
# Program crashes and shows ugly error message
#ATM Machines
#Common errors in Python:
'''Dividing by zero,Open afile that doesnot exist,wrong input example needs an name and we enter int'''
'''Jab aapke code mein error aaye aur aap ne khud koi plan nahi banaya us error ke liye — to Python ka apna system woh error pakad kar screen par message dikhata hai aur program band kar deta hai.'''
def divide(a,b):#calculator example
    result = a/b
    return result
x = divide(5,0)
print(x)#ZeroDivisionError: division by zero