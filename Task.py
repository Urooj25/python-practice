#task 1
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
#task 2 casefold()
txt = "Hello, and  welcome to my world."
x = txt.casefold()
print(x)
#center() task 3
txt = "banana"
x = txt.center(20)
print(x)    
#string.center task 4
txt = "Banana"
x = txt.center(8, "L")
print(x)
#task count() task 5
txt = "I love apples, apples are my favourite fruits"
x = txt.count("a")
print(x)
#task string.count(value,star,end) task 6
txt = ("I love apple, apple is my fav fruit")
x = txt.count("apple",1,15)
print(x)
# task 7 endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")     
print(x)     
#task 8
txt = "Hello, welcome to my world"   
x = txt.endswith(("world", "castle"))  
print(x)
#task
txt = "hELLO, welcome to my world"
x = txt.find("welcome")
print(x)
#task
txt = "Hello, welcome to my world" 
x = txt.find("e" , 5, 10)
print(x)
#format()
txt = "for only {price:.2f} dollers!"
print(txt.format(price = 49))
#named indexes
txt1 = "My name is {fname}, I' am {age} ".format(fname = "John", age = 36)
print(txt1)
#numbered indexes
txt2 = "My name is {0}, I' am  {1}".format("John", 36)
print(txt2)
#empty placeholders
txt3 = "My name is {}, I' am {}".format("John",36)
print(txt3)
#Boolean type 
x = True
print(type(x))
#compairon operators
print(10>9)
print(10==9)
print(10<9)
#Evaluate values and variables (importent in security domain)
x = "Hello"
y = 25
print(bool(x))
print(bool(y))#if variable is empty non or false it returns false
#Operators
x = 10
y = 5
#Floor division
print(x/y)
print(x//y)
#And and or operator convert to binary then add according to & operator
x = 3
x &= 2
print(x)
x = 5
x |= 2
print(x)

#post lab task
sentence = input("Enter your sentence:")
Words_to_Count = input("Enter word:")
y = sentence.find(Words_to_Count)

z = sentence.count(Words_to_Count)
print(y)
print(z)

if ("Words_to_Count" not in sentence):
 print("Word not found")
#post lab task 2
Email = input("Enter your Email:")
x = "@" in Email
y = "." in Email
z = Email.endswith(".com") or Email.endswith(".edu")

print(x)
print(y)
print(z)
#task 3 BY USING SPLIT
My_Email = "Ali123@gmail.com"
parts = My_Email.split("@")
Username = parts[0]
domain = parts[1]
print(Username)
print(domain)
#BY USING FIND
My_Email = "Ali124@gmail.com"
Find = My_Email.find("@")
Username = My_Email[ :Find]
Domain = My_Email[Find+1:]
print(Username)
print(Domain)



