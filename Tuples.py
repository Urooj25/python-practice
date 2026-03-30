x = ('Apple','Orange','Grapes')
print(x)
#Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))
print(type(thistuple))
#It is also possible to use the tuple() constructor to make a tuple.
fruits = tuple(("Apple"))#cannot create like this 
print(fruits)
#Access tuple item
x = ('Apple','Orange','Grapes','cherry','banana','waterlemon')
print(x[1])
print(x[-1])
print(x[-1:-4])#wrong bcz it moves from left to right
print(x[-4:-1])
print(x[-1:-4:-1])#star stop step
print(x[:4])
print(x[1:])
x = ('Apple','Orange','Grapes','cherry','banana','waterlemon')
if "kiwi" in x:
    print("yes")
else:
    print("no")
#Update tuple  Tuples are unchangeable, or immutable can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ('Apple','Banana','cherry')
y = list(x)
y[1] = "kiwi"

#can also used append 
y.append('Grapes')
y.remove('cherry')
print(y)
#Add tuples
x = (1,2,3)
y = (4,5,6)
x += y
print(x)#del is used to remove complete tuple
#Unpacking a tuple
x = ('Apple','Banana','cherry')
(green,yellow,blue) = x
print(green)
print(yellow)
print(blue)#agr values zayada hu tu* used kr lu more the 1  variable
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(red,*yellow) = fruits
print(red)
print(yellow)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(red,*middle,orange) = fruits
print(red)
print(middle)
print(orange)



