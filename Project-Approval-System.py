class Person:
 def __init__(myobject):
   myobject.Name = input("Enter your project name:")
   myobject.Language = input("Enter the name of the language you used for this project:")
 def greet(myobject):
        print("Hello"+ myobject.Name)
        if myobject.Language == "python":
         print("Congratulations, your project is approved")

        else :
         print("Sorry, python is requirement")


p1 = Person()
p1.greet()
