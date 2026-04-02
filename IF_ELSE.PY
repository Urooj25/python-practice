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