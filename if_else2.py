#If you have only one statement to execute, you can put it on the same line as the if statement.
a = 4
b = 6
if b > a: print("b is greater then a")
#Both if and else 
a = 7
b = 6
print("a") if a > b else print("b")
#Assign a Value With If ... Else
a = 7
b = 5
Bigger = a if a > b else b
print("Bigger is :", Bigger)
#Multiple Conditions on One Line
a = 330
b = 400
print("A") if a > b else print("=") if a == b else print("B")
#Mx value
a = 400
b = 500
max_value = a if a > b else b
print("max_value = " , max_value)
#task
username = ""
display_name = username if username else "Guest"
print("Welcome!", display_name)
#logical operaors
a = 200
b = 300
c = 400
if a < b and b < c:
    print("Both are true")

a = 200
b = 300
c = 400
if a < b or b > c:
    print("Both are true")
a = 200
b = 300
c = 400
if not a > b:
    print("This is not true")
#Combining multiple operators
age = int(input("Enter your age:"))
is_student = True
has_Discont_code = True
if age >= 18 and (is_student or has_Discont_code):
    print("Discount Applies!")
#Task 2
Temperature = 8
is_raining = False
is_weekend = True
if (Temperature > 20 and not is_raining) and is_weekend:
    print("Great day! for outdoor activities")
else:
    print("Not good day for Outing")
#User authentication check
username = input("Enter your name:")
Password = int(input("Enter your password:"))
is_verified = True
if username and Password and is_verified:
    print("Login Successful!")
else:
    print("Login Failed!")
#Range checking with logical operators:
Score = 102
if Score >= 0 and Score <= 100:
    print("Valid score")
else:
    print("Invalid score")
#Nested if
x = 16
if x > 10:
    print("Above 10")
    if x > 20:
        print("Also above 20")
    else:
        print("Not above 20")
#task
Age = 17
has_licenced = True
if Age >= 18:
    if has_licenced:
        print("You can drive")
    else:
            ("You need licenced")
else:
    print("You are too young to drive")
#Multiple level of nesting
Score = int(input("Enter you score:"))
Attendence = int(input("Enter your attendence:"))
is_submitted = True
if Score > 65:
    if Attendence >= 75:
        if is_submitted:
            print("pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but Attendence is low")
else:
    print("You are fail")
#Tak
Tem = 15
is_sunny = True
if Tem >= 20:
    if is_sunny:
        print("Weather is good")
else:
    print("The weather is not good")
#Shortcut used and
Tem = 15
is_sunny = True
if Tem >= 20 and is_sunny:
    print("Weather is good")
else:
    print("The weather is not good")
#Login validation
username = ""
password = 12345678
is_active = True
if username is not "":
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Pssword required")
else:
    print("Login failed")
#Pass statement
a = 33
b = 40
if a < b:
    pass
#
age = 16
if age > 18:
    pass
else:
    print("Access granted")
#Using in different 
Number = 6
if Number > 0:
    print("Positive value")
elif Number == 0:
    pass
else:
    print("The number is negative")
#While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.
def discount_amount(price):
    pass
