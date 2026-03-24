#python operators
#arthemetic
sum1 = 200
sum2 = 5
print(sum1+sum2)
print(sum2-sum1)
print(sum1*sum2)
print(sum1**sum2)
print(sum1/sum2)
print(sum1%sum2)
print(sum1//sum2)
#assignment operators
x = 5
x += 3
y = 5
y -= 3
z = 5
z *= 3
a = 5
a /= 5
b = 3
b **= 5
y == 5
y = 6
c = 7
c %= 5
d = 7
e = 7
d //= 5
e ^= 5#bitwise addition krta ha then return value#XOR Chnde vale like 1 to 0 and 0 to 1
f = 9
f &= 5# Addition Both bits must be 1 to get 1
g = 8

g |= 5#At least one bit must be 1 to get 1
h = 5
  
h <<= 3# first convert 5 to binary then Then — Shift all bits 3 places to the LEFT ex
#"""Original:   0 0 0 0 0 1 0 1   (5)
#Shift 1:    0 0 0 0 1 0 1 0
#Shift 2:    0 0 0 1 0 1 0 0
#Shift 3:    0 0 1 0 1 0 0 0   (40)""""
j = 6
j >>= 5#reverse
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k :=3)
#The walrus operators shorter code evaluate and assign same time
number = [1,2,3,4,5]
if (count := len(number)) > 3:
 print(f"list has {count} elements")
## Without := we need TWO lines
count = len(number)       # line 1 — assign
if count > 3:              # line 2 — check
    print(f"List has {count} elements")
#Comparison operators
X = 5
Y = 11
print(X>Y)
print(X<Y)
print(X==Y)
print(X!=Y)
print(X<=Y)
print(X>=Y)
#chaining Assignment
print(X<10>Y)
print(X<6>Y)
print(X>4 and Y<17)
#logical operators
print(5>3 and 5<6)
print(5<3 or 5>4)
print(not(5>3 and 10<17))
#identity operators
x = ["APPLE","BANANA"]
y = ["APPLE","BANANA"]
print(x is y)
print(x==y)
z = x
print(z == x)
print(z is x)
print (z is not y)
#Memorship in strings
print("BANANA" in x)
print("Grapes" not in x)
Z = "HELLO WORLD"
print("H" in Z)
#Bitwise operators ~ not operator reverse
#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0: