#python for loops
for x in "banana":
    print(x)
fruits = ["Apple","banana","orange"] 
for x in fruits:
    print(x)
#tasst 3
fruits = ["Apple","banana","orange"]
for x in fruits:
    print(x)
    if x == "banana":
        break
fruits = ["Apple","banana","orange"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#Continue
fruits = ["Apple","banana","orange"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#range
for x in range(6):
    print(x)
for x in range(2,6):
    print(x)
for x in range(3,33,3):
    print(x)
#else in for loops
for x in range(6):
    print(x)
else:
    print("finally finished")
#
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    ("Finally finished")
#nested loops
fruits = ["Apple","Banana","Cherry"]
cars = ["corolla","mehran","mercedes"]
for x in fruits:
    for y in cars:
        print(x,y)
#Code challenge
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
      break


  