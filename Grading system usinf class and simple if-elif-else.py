class Person:
     def __init__(self):
      self.Name = input("Enter your name:")
      self.Class = input("Enter your Class:")
      self.Marks = int(input("Enter your marks:"))


      if self.Marks >= 80:
       print("Grade is A")
      elif 70 <= self.Marks and self.Marks <80:
       print("Grade is B+")
      elif self.Marks >=60:
       print("Grade is B")
      else :
       print("Grade is C")


p1 = Person()