#Decorators let you add extra behavior to a function, without changing the function's code.
#Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "hello urooj"
print(myfunction())
#multiple
def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def myfunction():
    return "hello Urooj"
@changecase
def greeting():
    return "Hello"
print(myfunction())
print(greeting())
#Arguments in the Decorated Function
def changecase(func):
    def inner(x):
        return func(x).upper()
    return inner
@changecase
def myfunction(name):
    return "Hello  " + name
print(myfunction("John"))
#*args and **kwargs
def myfunction(func):
    def inner(*arg,**karg):
        return func(*arg,**karg).upper()
    return inner
@myfunction
def function(name):
    return "hello " + name
print(function("john"))
#Task
def myfunction(n):
    def changecase(fun):
        def myinner():
            if n == 1:
                a =  fun().upper()
            else:
                a = fun().lower
            return a
        return myinner
    return changecase
@myfunction(1)
def function():
    return "Hello linus" 
print(function())

#Multiple Decorators
        
