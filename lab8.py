# Creating and printing a dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing items using a key
brand_name = thisdict["brand"]
model_name = thisdict.get("model") # Using get() method 

# Checking length and data types 
print(len(thisdict)) 
complex_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"] # Values can be lists 
}

# Using the dict() constructor 
new_dict = dict(name="John", age=36, country="Norway")
# Updating a value
thisdict.update({"year": 2020})

# Adding a new item 
thisdict["color"] = "white"

# Removing items 
thisdict.pop("model")       
thisdict.popitem()          
del thisdict["brand"]       
# thisdict.clear()          ]
# Getting keys, values, and items 
keys = thisdict.keys()
values = thisdict.values()

# Looping through a dictionary 
for x, y in thisdict.items():
    print(x, y) # Prints both keys and values 
#Lab Task
# Storing student marks
students = {
    "Urooj": 85,
    "Amna": 84,
    "Zain": 78,
    "Fatima": 88
}

# 1. Calculate Average Marks
total_marks = sum(students.values())
average = total_marks / len(students)
print(f"Average Marks: {average}")

# 2. Find Topper Student
topper = max(students, key=students.get)
print(f"Topper Student: {topper} with {students[topper]} marks")
#Task 2
# item -> [price, quantity]
store = {
    "Laptop": [50000, 5],
    "Mouse": [1500, 10],
    "Keyboard": [2500, 8]
}

print("Inventory Value Breakdown:")
for item, data in store.items():
    price = data[0]
    quantity = data[1]
    total_value = price * quantity

    print(f"{item}: Total Value = {total_value}")
#task 3
student_records = {}

# 1. Take input from user
n = int(input("How many students do you want to add? "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    student_records[name] = marks

# 2. Search for a student's marks
search_name = input("\nEnter the name of the student to search for marks: ")

if search_name in student_records:
    print(f"{search_name}'s marks: {student_records[search_name]}")
else:
    print("Student record not found.")