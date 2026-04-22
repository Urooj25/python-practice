students = {"Urooj","Amna","Komal"}
names = iter(students)
print(next(names))
print(next(names))
print(next(names))
#Even strings are iterable objects, and can return an iterator:
x = "Urooj Fatima"
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
#We can also use a for loop to iterate through an iterable object:
x = "banana"
for x in "banana":
    print(x)
#The for loop actually creates an iterator object and executes the next() method for each loop.
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a 
        self.a +=1
        return x
myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#StopIteration
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
      if self.a <=20:
        x = self.a 
        self.a +=1
        return x
      else:
        raise StopIteration
myclass = mynumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)