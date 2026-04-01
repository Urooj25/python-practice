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
Showroom = {
    "Name" : "Urooj",
    "Class" : "Charlie",
    "year" : 2,
    "passed" : True,
    "year" : "Second",
    "friends" : ("Amna","Komal")
}
print(Showroom)
print(len(Showroom))# 3
#Constructor
Class = dict(Name = "Urooj", Class = "C", subject = "Sience")
print(Class)
print(type(Class))

