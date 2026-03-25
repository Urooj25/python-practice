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
#Change List items