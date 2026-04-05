#*args and **kwargs allow functions to accept a unknown number of arguments.(tuple)
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
# 
def my_function(*numbers):
 if len(numbers) == 0:
  return none
 max_num = numbers[0]
 for num in numbers:
    if num > max_num:
        max_num = num
 return max_num
print(my_function(3,7,2,9,1))
#Using **kwargs to accept any number of keyword arguments:
def my_function(**kids):
    print("his last name is " + kids["lname"])
my_function(fname = "Toms", lname = "refses")
#The **kwargs parameter allows a function to accept any number of keyword arguments.(Dictionary bnata ha)
def my_function(**variables):
    print("type:", type(variables))
    print("Name:",variables["name"])
    print("age is : ", variables["age"])
    print("city is: ",variables["city"])
    print("all data is", variables)
my_function(name= "urooj", age = 21, city = "wahcantt")#Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
#If you have values stored in a list, you can use * to unpack them into individual arguments:
def my_function(a,b,c):
    return a + b + c
numbers = [1,2,3]
result = my_function(*numbers)#unpack tuple
print(result)
#
def my_function(name, sirname):
    print("hello "  ,name , sirname)
person = {"name":"urooj", "sirname": "fatima"}
my_function(**person)#unpack dictionary


