#Ordered since 3.7 version,changable,not allowed duplicates
#Dictionaries are used to store data values in key:value pairs.
showroom = {
    "Brand" : "Corolla",
    "Model" : 1997,
    "Color" : "Red"
}
print(type(showroom))
print(showroom["Brand"])
print(showroom["Color"])
#Duplicate will rewrite on existing
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")
}
print(Class)
print(len(Class))# 3
#Constructor
Class = dict(Name = "Urooj", Class = "C", subject = "Sience")
print(Class)
print(type(Class))
#Access items ,.get()
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
x = Class.get("year")
print(x)
print(Class["friends"])
#.keys()return full dict
x = Class.keys()
print(x)
#
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
x = Class.keys()
print(x)#before update
Class["Rollno"] = 158137
print(x)
#The values() method will return a list of all the values in the dictionar
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
x = Class.values()
print(x)
Class["strenght"] = 43
print(x)
#The items() method will return each item in a dictionary, as tuples in a list.
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
x = Class.items()
print(x)
Class["Dep"] = "Electrical"
print(x)
#Check if Key Exists
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
if "Name" in Class:
    print("Student is present")
#change dic
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
Class["year"] = 5
print(Class)
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
Class.update({"Class" : "Beta"})
print(Class)
#Remove items
#The pop() method removes the item with the specified key name:
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
Class.pop("friends")
print(Class)
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
Class.pop("friends")
Class.popitem()
print(Class)
#The del keyword removes the item with the specified key name:
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
del Class["Class"]
print(Class)
#The del keyword can also delete the dictionary completely:
#The clear() method empties the dictionary:
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")
}
Class.clear()
print(Class)
#Loop Through a Dictionary return key
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
for x in Class:
    print(x)
    #to return value as well
    Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
for x in Class:
    print(Class[x])
    #use method.Value
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
for x in Class.values():
    print(x)
#to return key
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
for x in Class.keys():
    print(x)
#return both keys and values
Class = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")}
for x in Class.items():
    print(x)








