def my_function():
    print("Hello from my function")
my_function()
#can call the same function multiple times
my_function()
#without function repitition
temp = 32
celsius1 = (temp - 32)*5/9
print(celsius1)
temp = 90
celsius2 = (temp - 32)*5/9
print(celsius2)
#with function
def fahrenhite_to_celsius(fahrenhite):
    return(fahrenhite-32)*5/9
print(fahrenhite_to_celsius(77))
print(fahrenhite_to_celsius(90))
#A function that returns a value:
def get_greeting():
    return "Hello from a greeting"
message = get_greeting()
print(message)
#can use the returned value directly
def greeting():
    return "Hello world"
print(greeting())#If a function doesn't have a return statement, it returns None by default
