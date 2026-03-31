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