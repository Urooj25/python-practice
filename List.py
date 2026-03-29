Thislist = ["Apple","Orange","Banana"]
print(Thislist)#changeable,Allow dublicates,ordered
#Allow dublicates
My_list = ["Apple", "Bananan", "Grapes", "Apple"]
print(My_list)
#list len
My_list = ["Apple", "Bananan", "Grapes", "Apple"]
print(len(My_list))
#List items can be of any data type:
x = [1,2,3,4,5]
y = [True,False,True]
z = ["Apple", "Banana"]
a = ["Apple",26 ,True,30.5, "Banana"]
print(x)
print(y)
print(z)
print(type(a))
#Using the list() constructor to make a List:
LIST = list(("Apple","  Banana"))
print(LIST)
#Access list items
print(LIST[1])
#NEgative i ndexing print last item
print(LIST[-1])
#Range of indexes
print(a[1:3])
print(a[ :4])
print(a[2:])
print(a[-4:-1])
#if condition
Fruits = ["Apple","Banana","Grapes"]
if "Apple" in Fruits:
    print("Yes, Apple is present")
#Change List
Fruits = ["Apple","Banana","Grapes"]
Fruits[2] = "Cherry"
print(Fruits)
Fruits = ["Apple","Banana","Grapes"]
Fruits[1:3] = "Onion", "Potato", "Tomato"
print(Fruits)
#Replace any value
Fruits = ["Apple","Banana","Grapes"]
Fruits[1:2] = ["cheery","Orange"]

print(Fruits)
#Insert itemsThe insert() method inserts an item at the specified inde
NUMBERS = [1,2,3,4,5]
NUMBERS.insert(3,"Urooj")
print(NUMBERS)
#Add list itemms
Fruits = ["Apple","Banana","Grapes"]
Fruits.append("Cherry")
print(Fruits)
#Add elements of two list
Fruits = ["Apple","Banana","Grapes"]
NUMBERS = [1,2,3,4,5]
Fruits.extend(NUMBERS)
print(Fruits)
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Fruits = ["Apple","Banana","Grapes"]
NUMBERS = (1,2,3,4,5)
Fruits.extend(NUMBERS)
print(Fruits)
#Remove list items

Fruits = ["Apple","Banana","Grapes"]#.remove() method is designed to remove only the first occurrence of the specified value 

Fruits.remove("Apple")
print(Fruits)
#Remove Specified Index pop()
Fruits = ["Apple","Banana","Grapes"]
Fruits.pop(1)
print(Fruits)
#If you do not specify the index, the pop() method removes the last item.
#del remove
NUMBERS = [1,2,3,4,5]#ERROR BCS TUPLE KO KRRHI THI

del NUMBERS
#The clear() method empties the list.
NUMBERS = [1,2,3,4,5]
NUMBERS.clear()
print(NUMBERS)
#Loop through a list
Names = ["Urooj","Ali","Amna","Komal"]
for x in Names:
    print(x)#error on 
#Loop Through the Index Numbers
Names = ["Urooj","Ali","Amna","Komal"]
for i in range(len(Names)):
    print(Names[i])
    #Using a While Loop
    Names = ["Urooj","Ali","Amna","Komal"]
    i = 0
    while i < len(Names):
        print(Names[i])
        i = i+2
#A short hand for loop that will print all items in a list:
Names = ["Urooj","Ali","Amna","Komal"]
[print(x) for x in Names]

#List Comprehension
Names = ["Urooj","Ali","Amna","Komal"]
newlist = [ ]
for i in Names:
    if "U" in i:
        newlist.append(i)
print(newlist)
#Short cut
Names = ["Urooj", "Ali", "Amna", "Komal"]
newlist = [i for i in Names if "U" in i]
print(newlist)
Names = ["Urooj", "Ali", "Amna", "Komal"]
newlist = [x.upper() for x in Names]
print(newlist)
newlist = [i for i in Names if i != "Urooj"]
print(newlist)
#iterable
newlist = [x for x in range(10)]
print(newlist)
#with codition [expression  for item in iterable  if condition]
newlist = [x for x in range(10) if x>5]
print(newlist)
Names = ["Urooj", "Ali", "Amna", "Komal"]
newlist = ["Hello" for x in Names]
print(newlist)
Names = ["Urooj", "Ali", "Amna", "Komal"]
newlist = [x if x != "Urooj" else  "Warrior" for x in Names]
print(newlist)
#Sort list
Names = ["Urooj", "Ali", "Amna", "Komal"]
Names.sort()#Arrange in assecening order
print(Names)
NUMBERS = [1,4,3,3,2,5]
NUMBERS.sort()
print(NUMBERS)
#Descending sort(reverse = True) pahle sort phir reverse
Names = ["Urooj", "Ali", "Amna", "Komal"]
NUMBERS = [1,4,3,3,2,5]
Names.sort(reverse = True)
print(Names)
NUMBERS.sort(reverse = True)
print(NUMBERS)
#Customize Sort Function Apna rule
def Student(x):
    return len(x)
Name = ["Urooj", "Ali", "Amna", "Komal"]
Name.sort(key = Student)
print(Name)
#abs convert + into -
def myfun(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfun)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#Capital letters pahle aate ha
# if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#return same
print(thislist)
#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Copy a ListYou cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method list().

thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = list(thislist)
print(mylist)#Two different list with same variables
#You can also make a copy of a list by using the : (slice) operator.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = thislist[:]
print(mylist)#fav
#Join Two Lists






