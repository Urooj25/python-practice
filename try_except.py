#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
    print(x)
except:
    print("An exception occured")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello world")
except:
    print("something went wrong")
else:
    print("There is no error")
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print("Hello world")
except:
    print("something went wrong")
finally:
    print("try_except is finished")
#This can be useful to close objects and clean up resources:
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")#yhi print hu gha bcz mry pass file hi nhi ha'
#As a Python developer you can choose to throw an exception if a condition occurs.
#To throw (or raise) an exception, use the raise keyword.
x = -1
if x < 0:
    raise Exception("sorry, no numbers below zero")
#You can define what kind of error to raise, and the text to print to the user
x = "hello"
if not type(x) is int:
    raise TypeError("only integers are alloed")
