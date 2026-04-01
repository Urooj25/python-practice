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






