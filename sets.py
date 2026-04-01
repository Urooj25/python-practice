people = {"Amna","Urooj","Komal"}
print(type(people))
#Duplicates remove
number = {1,2,2,3,3,4,5,4,6}
print(number)
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
number = {1,2,3,True,5,7,9,4,3,10,9,8}
print(number)
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
Numbers = {1,2,3,4,5,False,6,7,8,9,10,True}
print(Numbers)
Mix = {1,2,3,True,"Urooj"}
print(Mix)
#Use constructer
Grocery = set(("oil","Ghee","Wheat","Rice"))
print(Grocery)
print(type(Grocery))
#Access set items
#You cannot access items in a set by referring to an index or a key. but can used loop
Numbers = {1,2,3,4,5,False,6,7,8,9,10,True}
for x in Numbers:
    print(x)
# check
Grocery = set(("oil","Ghee","Wheat","Rice"))
print("Suger" in Grocery)#Bool return
Grocery = set(("oil","Ghee","Wheat","Rice"))
print("Suger" not in Grocery)#Bool return
#We cannot change items in set but can add
#add set items .add() cannot change but add
Grocery = set(("oil","Ghee","Wheat","Rice"))
Grocery.add("Seeds")
print(Grocery)
#update()
Grocery = set(("oil","Ghee","Wheat","Rice"))
Numbers = {1,2,3,4,5,False,6,7,8,9,10,True}
Grocery.update(Numbers)
print(Grocery)
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

Grocery = set(("oil","Ghee","Wheat","Rice"))
Numbers = [1,2,3,4,5]
Grocery.update(Numbers)
print(Grocery)
#To remove an item in a set, use the remove(), or the discard() method.
Grocery = set(("oil","Ghee","Wheat","Rice","seed"))
Grocery.remove("seed")
Grocery.discard("oil")
print(Grocery)
#If the item to remove does not exist, discard() will NOT raise an error but remove will give.
#pop()can remove random value so no good to used
Grocery = set(("oil","Ghee","Wheat","Rice","seed"))
x = Grocery.pop()
print(x)#gives remove item
print(Grocery)
#The clear() method empties the set:
Grocery = set(("oil","Ghee","Wheat","Rice","seed"))
Grocery.clear()
print(Grocery)
#del delete completly
Grocery = set(("oil","Ghee","Wheat","Rice","seed"))

print(Grocery)
#Loop set
Fruits = {"Apple","Banana","Kiwi"}#follow hash order
for x in Fruits:
    print(x)
#Frozenset Unlike sets, elements cannot be added or removed from a frozenset.

Fruits = frozenset({"Apple","Banana","Kiwi"})
print(Fruits)
print(type(Fruits))
#join methods .union(), \
set1 = set(("oil","Ghee","Wheat","Rice","seed"))
set2 = Numbers = {1,2,3,4,5,False,6,7,8,9,10,True}
set3 = set1.union(set2)
se3 = set1 | set2
print(set3) 
print(se3)
#Join Multiple Sets
set1 = set(("oil","Ghee","Wheat","Rice","seed"))
set2 = Numbers = {1,2,3,4,5,False,6,7,8,9,10,True}
set3 = {True,False,1,"Urooj"}
set4 = set1.union(set2,set3)
se4 = set1 | set2 | set3
print(set4)
print(se4)
#Join set and tuple
set1 = set(("oil","Ghee","Wheat","Rice","seed"))
x = (1,2,3,4,5)
print(set1.union(x))
#update() Both union() and update() will exclude any duplicate items
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
x.update(y)
print(x)
#The intersection() and & method will return a new set, that only contains the items that are present in both sets.
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
x = x.intersection(y)
y = x & y
print(x)
print(y)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
x.intersection_update(y)
print(x)
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
z = x.difference(y)
print(z)
#Another way
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
z = x - y
print(z)
#.difference_update
x = {1,3,45,5,5}
y = {3,4,5,6,7,4}
x.difference_update(y)
print(x)
#Symmetric Differences,^
x = {1,3,45,5,5}
set2 = {False, "google", 1, "apple", 2, True}
z = x.symmetric_difference(set2)
k = x ^ set2
print(z)
print(k)
x = {1,3,45,5,5}
set2 = {False, "google", 1, "apple", 2, True}
x.symmetric_difference_update(set2)

print(x)
#code challenge
colors = {"red","green","blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))




