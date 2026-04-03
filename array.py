#Arrays are used to store multiple values in one single variable bu using library numpy
cars = ["ford","corolla","mehran"]
print(len(cars[0]))
cars[1] = "mercedes"
cars.append("honda")
cars.pop(2)#indexed base
cars.remove("ford")#Purpose: Removes an element by value (not by index)Key point: Only the first occurrence is removed
#If the value is not found → Python throws ValueError
for x in cars:
    print(x)
    print(cars)
#Code challenge
cars = ["ford","Volvo","BMW"]
print(cars[0])
cars[1] = "Toyoto"
print(cars)

