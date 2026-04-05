#*args and **kwargs allow functions to accept a unknown number of arguments.
def my_function(*kids):
    print("The youngest child is " + kids[1])
my_function("sara","amna","zara")
#arg 
def my_function(*args):
    print("type: " ,type(args))
    print("first argument: ", args[0])
    print("2nd argument: " , args[1])
    print("all arguments", args)
my_function("urooj","Komal","sana")
#Using *args with Regular Arguments
#Regular parameters must come before *args:
def my_function(greeting,*names):
    for name in names:
        print(greeting,name)
my_function("hello","sara","amna")
#Practical Example with *args
def my_function(*numbers):
    total = 0
    for num in numbers:
     total += num
    return total
print(my_function(1,2,3))
print(my_function(10,20,30,40))
print(my_function(5))
#finding the maximum value


