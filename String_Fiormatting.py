txt = f"The price is 49 doller"
print(txt)
price = 59
x = f"the price is {price} dollers"
print(x)
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59
x = f"the price is {price:.2f} dollers"
print(x)
txt = f"the price is {95:.2f} doller"
print(txt)
price = 59
x = f"the price is {5*5} dollers"
print(x)
price = 50
tax = 0.25
txt = f"the price is {price + (price * tax) } dollers"
print(txt)
#You can perform if...else statements inside the placeholders:
price = 49
txt = f"the price is {'Expensive'if price > 50 else 'cheap' }"
print(txt)
#You can execute functions inside the placeholder:
fruit = "apple"
txt = f"I love { fruit.upper()}"
print(txt)
#The function does not have to be a built-in Python method, you can create your own functions and use them:
def myconverter(x):
    return x * 0.3048
txt = f"the plane if flying at {myconverter(3000)} meter altitude"
print(txt)
#Use a comma as a thousand separator:
price = 50000
txt = f" the price is {price:,} dollers"
T = f" the price is {50:<5} dollers"#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
print(txt)
print(T)
A = f"I have {5:>2} books"
print(A)
B = f"I have {10:^4} chocolates"
print(B)
C = f"This places asign to let most {5:=3}position"
print(C)
D = f"use a plus sign to indicite result is {-4:+4} positive or negative"
print(D)
E = f"Use a minus sign for negative{1:-5} values only"
print(E)
f = f"Use a space to insert an extra space before positive numbers{4:4} (and a minus sign before negative numbers)"
print(f)
G = f"Use a underscore{5000:_} as a thousand separator"
print(G)
E = f"Binary format{5:b}"
print(E)
H = f"Converts the value into the corresponding {65:c} Unicode character"
print(H)
I = f"Decimal format{56:d}"
print(I)
J = f"Scientific format, with a lower case e{6:e}"
print(J)
L = f"Scientific format, with an upper case E{5:E}"
print(L)
M = f"Scientific format, with a lower case e{5:e}"
print(M)
N = f"Fix point number format{4:f}"
print(N)
O = f"Fix point number format, in uppercase format (show inf and nan as INF and NAN){67:F}"
print(O)
P = f"General format {56:g}"
print(P)
Q = f"General format (using a upper case E for scientific notations){99:G}"
print(Q)
R = f"Octal format{56:o}"
print(R)
S = f"Hex format, lower case{56:x}"
print(S)
T = f"Hex format, upper case{56:X}"
print(T)
U = f"Number format{56:n}"
print(U)
V = f"Percentage format{67:%}"
print(V)
#String format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
x = 3
y = 50
z = 49
txt = "we need potato {0} and tomato {1} for {2:.2f}dollers"
print(txt.format(x,y,z))
#Also, if you want to refer to the same value more than once, use the index number:
age = 21
name = "Urooj"
txt = "MY name is {1}.{1} is {0} yaer old"
print(txt.format(age,name))
#Named Indexes
cars = "I have a {carname} and it is a{model}"
print(cars.format(carname = "corrolla", model =" Mustang" ))