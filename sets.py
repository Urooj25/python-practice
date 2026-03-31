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





