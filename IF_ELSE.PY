#Python if statement
a = int(input("Enter a number:"))
b = int(input("Enter second number:"))
if a >= b:
    print("This is Greater number")
else:
    print("This is a smaller number")
#task 2
a = int(input("Enter a number:"))
if a > 0:
    print("Number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")
#Multiple statement 
age = int(input("Enter your age:"))
if age >= 18:
    print("Yes you can vote 😊", "You have full legal rights🙌", "take your decision wisely🧠", sep="\n")
else:
    print("Wait to turn into 18 to vote")
#boolian
Is_login = True
Email = str(input("Enter you Email:"))
if Is_login and Email != "":
    print("Welcome back!")
else:
    print("Sorry, session is out")
#Elif
a = int(input("Enter number:"))
b = int(input("Enter number 2:"))
if a > b:
    print("This number is greater then other")
elif a == b:
    print("Both are equal")
#Multiple Elif 
Marks = int(input("Enter your marks:"))
if Marks >= 80:
    print("Congratulations, your grade is A")
elif Marks < 80 and Marks >= 70:
    print("Congratulations, your grade is B")
elif Marks > 60 and Marks <= 70:
    print("Your grade is C+")
else:
    print("You are fail")
#
Age = int(input("Enter your age:"))
if Age >= 60:
    print("You are senior citizen")
elif Age >= 50:
    print("You are not too old ")
elif Age >= 40:
    print("You are young man")
elif Age >= 20 and Age < 40:
    print("You are Adult")
else:
    print("You are too immature ")
#days check
day = int(input("Enter a Day:"))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("friday")
else:
    print("Weekend")
#checking even and odd
a = int(input("Enter a number:"))
if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Temperature check
Temperature = int(input("Enter todays temperature:"))
if Temperature > 30:
    print("Its hot outside")
elif Temperature > 20:
    print("Its warm outside")
elif Temperature > 10:
    print("Its cold outside")
    
else:
    print("Its freezing Temp outside")
#login
Username = input("Enter your username:")
Password = (input("Enter your password:"))
if len(Username) > 0 and len(Password)  > 0:
    print(f"Hello, {Username}!")
else:
    print("Please enter valid username and password")
