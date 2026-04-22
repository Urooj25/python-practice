thisset = {"Apple","banana","cherry"}
print(thisset)
#Duplicates are not allowed
thisset = {"Apple","banana","cherry","Apple"}
thisset = {"Apple","banana","cherry", True,1,2}#true = 1 False = 0
print(thisset)
thisset = {"Apple","banana","cherry", False,0,2}
print(thisset)
print(len(thisset))
print(type(thisset))
#The setconstructor
thisset = set(("Apple","banana","cherry", False,0,2))
print(type(thisset))
#python access set items
thisset = set(("Apple","banana","cherry", False,0,2))
for x in thisset:
    print(x)#unordered
print("banana" in thisset)
print("banana" not in thisset)
#add items items unchangable can be add or remove but cant replace
thisset = set(("Apple","banana","cherry", False,0,2))
thisset.add("orange")
print(thisset)
#Add sets .update
thisset = set(("Apple","banana","cherry"))
tropical = {"Pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
#list+sets etc
thisset = {"Apple","banana","cherry"}
tropical = ["Pineapple","mango","papaya"]
thisset.update(tropical)
print(thisset)
thisset = {"Apple","banana","cherry"}
tropical = ("Pineapple","mango","papaya")
thisset.update(tropical)
print(thisset)
#remove(),disard()
thisset = {"Apple","banana","cherry"}

thisset.discard("pineapple")#if remove used error
#pop()
thisset = {"Apple","banana","cherry"}
thisset.pop()
print(x)
print(thisset)
thisset = {"Apple","banana","cherry"}
thisset.clear()
print(thisset)
print(type(thisset))
thisset = {"Apple","banana","cherry"}
print(thisset)# if del used error bcz thisset is delete
#union 
set1 = {"Apple","banana","cherry"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
set1 = {"Apple","banana","cherry"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)
#join multiple sets
set1 = {"Apple","banana","cherry"}
set2 = {1,2,3}
set3 = {"A","B"}
set4 = set1.union(set2,set3)
print(set4)
X = {"A","B","C"}
Y = (1,2,3)
Z = X.union(Y)
print(Z)
#update
set1 = {"Apple","banana","cherry"}#first must bhi set
set2 = (1,"Apple","Banana")
set1.update(set2)
print(set1)
#intersection
set1 = {"Apple","banana","cherry"}#id &used dont work on different data types
set2 = (1,"Apple","Banana")
set3 = set1.intersection(set2)
print(set3)
set1 = {"Apple","banana","cherry"}#id &used dont work on different data types
set2 = {1,"Apple","Banana"}
set3 = set1 & set2
print(set3)
set1 = {"Apple","banana","cherry"}#id &used dont work on different data types
set2 = {1,"Apple","Banana"}
set1.intersection_update(set2)#memory saving
print(set1)
set1 = {"Apple","banana","cherry",True,False}
set2 = {1,"Apple","Banana",1,0}
set1.intersection_update(set2)
print(set1)
#difference()
set1 = {"Apple","banana","cherry"}
set2 = {"Google","Microsoft","Apple"}
set3 = set1.difference(set2)
print(set3)
set1 = {"Apple","banana","cherry"}
set2 = {"Google","Microsoft","Apple"}
set1.difference_update(set2)
print(set1)
#symmetric difernce uncommen items
set1 = {"Apple","banana","cherry"}
set2 = {"Google","Microsoft","Apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#frozenset
x = frozenset({"Apple","Banana","cheery"})#cant add or remove or clear (gives error)

print(x)
print(type(x))#used for security purpose

#Lab tasks
math_students = {"Amna","Urooj","Noor"}
cs_students = {"Maryam","komal"}
both = math_students | cs_students
add.both("kashf")
one = math_students & cs_students
print(both)
print(one)
both.discard("Amna")
both.remove("Urooj")
both.pop()
print(both)





























