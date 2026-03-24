#boolians
print(15>6)
print(15==14.5)
print(15<10)
#used in if condition 
a = 200
b = 150
if(a>b):
    print("a is greater then b")
else:
    print("Bis greater then a")

#Bool()allows you to evaluate any value
print(bool("Hello word"))
print(bool(34))
#Return false anything empty
print(bool())
#evaluate variables
x = "Urooj"
y = 24
print(bool(x))
print(bool(y))
"""Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""
print(bool("abc"))
print(bool(25))
print(bool(["Apple","Orange","Grapes"]))
#Some values are false
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(0))
print(bool(None))
print(bool(False))
#Another importent case
#evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0#false
myobj = myclass()     
print(bool(myobj))  
#function can also create boolean
def myfunction():
    return False#error if wriiten in small alphabet
print(myfunction())
#boolean with the if
def MYFunction():
    return False
if MYFunction():
    print("Yes") 
else:
    print("NO")  
#built in function to check boolian isinstance()
z = "Urooj"
print(isinstance(z,int))#False
#Code challenge
print(10>9)
print(10==9)
print(bool("Hello"))
print(bool(0))