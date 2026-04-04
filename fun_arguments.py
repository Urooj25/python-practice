def my_function(fname):#parameter
    print(fname  + "fatima")#direct output day gha but return tb used krta jb kuch store krwa kr print krwana hu
my_function("Urooj ") 
my_function("Amna ")#Argument
#If your function expects 2 arguments, you must call it with exactly 2 arguments.
def my_function(Name,sirname):
    print(Name + " " + sirname)
my_function("Urooj" , "Fatima")
#can assign default values to parameters. If the function is called without an argument, it uses the default value
def my_function(Name = "Amna"):
    print("Hello", Name)
my_function("Urooj")
my_function()#default value
#3task 2
def my_function(country = "Pakistan"):
    print("I am from " , country)
my_function("Norway")
my_function()
#can send arguments with the key = value syntax.
def my_function(animal,name):
    print("My " , animal +" name's is ", name)
my_function(animal = "dog", name = " tommy")
#This way, with keyword arguments, the order of the arguments does not matter.
def my_function(animal,name):
    print("I have a ", animal)
    print("MY ", animal + "Name is ", name )
my_function(name = "tommy", animal = "Dog ")
#When we call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:
def my_function(animal,name):
    print("I have a ", animal)
    print("MY ", animal + "Name is ", name )
my_function("dog ","tommy ")
#changing argument change result
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy ", "dog ")
#positional argument present before keyword argument
def my_function(Animal,Name,Age):
    print("I have a ", Animal + " named " , Name + " His age is ", Age)
my_function("dog", Name = "buddy" , Age = 5)
#can send any data type as an argument to a function (string, number, list, dictionary, etc.)
def my_function(fruits):
    for fruits in fruits:
        print(fruits)
fruits = ["Apple","Banana","cherry"]
my_function(fruits)
#Sending a dictionary as an argument:
def my_function(person):
    print("Name :" , person["Name"])
    print("Age: " , person["age"])
my_person = {"Name" : "Urooj", "age" : 21}
my_function(my_person)
#Functions can return values using the return statement:
def myfunction(x,y):
    return x + y
result = myfunction(5,6)
print(result)
#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
    return ["Apple","banana","cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
#A function that returns a tuple
def my_function():
    return (10,20)
x, y = my_function()
print("x:", x, "y:" ,y )
#To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
    print("hello ",name )
my_function("Urooj")
#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(name):
    print("hello ",name )
my_function(name = "Urooj")

#To specify that a function can have only keyword arguments, add *, before the arguments
def my_function(*,name):
    print("hello ",name )
my_function(name = "Urooj")
#Without
def my_function(name):
    print("hello ",name )
my_function("Urooj")
#Combining Positional-Only and Keyword-Only
def my_function(a,b,/,*,c,d):
    return a + b + c + d
result = my_function(5,10, c = 16, d = 20)
print(result)
