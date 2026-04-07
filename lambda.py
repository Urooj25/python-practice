x = lambda a : a + 10
print(x(5))#behave like a function in a smaller way
#
x = lambda a,b : a*b
print(x(5,6))
x = lambda x,y,z : x+y+z
print(x(5,3,2))
#Agar a future input ke liye function return karna hai, lambda ya nested function use karo
def myfunction(n):
    return lambda a : a*n
mydoubler = myfunction(3)
mytripler = myfunction(3)
print(mydoubler(2))
print(mytripler(11))#Custom multipliers,ML mein scaling,Dynamic functions banana
#Lambda with Built-in Functions
#The map() function applies a function to every item in an iterable:
numbers = [1,2,3,4,5]
double = list(map(lambda x: x * 2 , numbers))
print(double)
#The filter() function creates a list of items for which a function returns True:
#Filter out odd numbers from a list:
y = [1,2,3,4,5,6,7,8,9]
filters = list(filter(lambda x: x % 2 != 0,y))
print(filters)
#The sorted() function can use a lambda as a key for custom sorting:
students = [("sans",25),("amna",21),("komal",21)]
students_soted = sorted(students,key=lambda x: len(x))#lenght according to age
print(students_soted)
#
students = [("sans",25),("amna",21),("komal",21)]
students_soted = sorted(students,key=lambda x: (x[1]))#sort according to age
print(students_soted)


