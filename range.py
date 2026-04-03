x = range(9)
print(x)
print(list(x))
x = range(1,11)
print(list(x))
print(x)
x = range(3,33,3)
print(x)
print(list(x))
#loop
for i in range(6):
    print(i)
#The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
#Therefore, ranges are often converted to lists for display.

print(list(range(2,12,2)))
print(list(range(10)))
print(list(range(2,11)))
#Slicing Ranges
x = range(10)
print(x[2])
print(x[:3])
#Membership Testing
x = range(0,10,2)
print(len(list(x)))
print(6 in x)
print(7 in x)
#Code challenge
for x in range(6):
 print(x)
for y in range(2,6):
 print(y)

