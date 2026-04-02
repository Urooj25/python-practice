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