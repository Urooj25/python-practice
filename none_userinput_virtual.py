x = None
print(type(x))
result = None
if result is None:
    print("No result")
else:
    print("Result is ready")
result = None
if result is not None:
    print("No result")
else:
    print("Result is ready")
#None evaluates to False in a boolean context.
print(bool(None))
#A function without a return statement returns None
def myfunction(x):
    x = 5
    return x
x = myfunction(x)
print(x)

    
