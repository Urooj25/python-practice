#Lab tasks
x = 5
y = 3
print(x==y)
#task2
x = 5 
y = 3
print(x != y)
#task
x = 5
y = 3
print(not(x > 3 and  x < 10))
x = 5
print(x < 5 <10)
x = 5
print(x < 5 or x > 10)
#identity operators check memory address
x = ["apple","banana"]
y = ["apple","banana"]
z = x
print(x is y)
#Task2
x = ["apple","banana"]
y = ["apple","banana"]
print(x == y)#check value
print(x is y)#Check address
#Membership operators in , not
fruits = ["apple","banana","cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)
#task
text = "Hello world"
print("H" in text)#True
print("Hello" in text)#True
print("z" not in text)#True
#task bitwise operator
print(6 & 3)#binary coversion then add
print(6 | 3)
print(6 ^ 3)
print(~3)#flip the bit if 0 end num + if 1 then _
print(3 << 2)#2 ki power n may multiplication right shift3*2^2
print(8 >> 2) #left shift 2 ki power n may diviosn 8/2^2 last bit neglect after  shift
#Lab tasks 1
Names = ["Urooj","Amna","komal"]
username = input("Enter your name :")
password = input("Enter your 8 character password: ")
print(username in Names)
print(len(password))
print("@" in password)

#lab task 2
x = input("Enter your list 1:").split()
y = input("enter your list 2:").split()
print(x == y)
print( x is y)

#lab task 3
n = int(input("Enter a num:"))
print(n << 2)
print(n >> 1)
print(~n)

