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
#User input
print("Enter your name:")
name = input()
print(f"my name is: {name}")
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
#To find the square root, the input has to be converted into a number:
import math
x = input("Enter a number:")
y = math.sqrt(float(x))
print(f"the square root of {x} is {y}")
#validate input
y = True
while y == 0:#Loop kbhi chal hi nhi
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except:
        print("Wrong input, try again")
print("Thank you")


