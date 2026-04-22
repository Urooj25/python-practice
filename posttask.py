math_students = {"Amna","Urooj","Noor"}
cs_students = {"Maryam","komal"}

# 1. Both courses
both = math_students & cs_students

# 2. Only one course
one = math_students ^ cs_students

# 3. Add new student
math_students.add("kashf")
cs_students.add("kashf")

print("Both:", both)
print("Only one:", one)

# 4. Remove safely
math_students.discard("Amna")   # safe
cs_students.remove("komal")     # will remove, error if not present

# 5. pop()
removed = math_students.pop()
print("Popped:", removed)

print("Final math set:", math_students)
#task 2
data = [10, 20, 30, 20, 40, 10, 50]

# 1. Convert list → set
convertset = set(data)

# 2. Remove faulty readings
convertset.difference_update({20, 30})

# 3. Add new readings (update works on set)
convertset.update({120})

# 4. Convert back to list
againlist = list(convertset)

print(againlist)
#Task 3
user1 = {"AI", "ML", "Cybersecurity"}
user2 = {"ML", "Data Science", "IoT"}

# 1. Common
print("Common:", user1 & user2)

# 2. New for user1
print("New for user1:", user2 - user1)

# 3. Unique
print("Unique:", user1 ^ user2)

# 4. Remove
user1.remove("AI")
user2.discard("Blockchain")

print("Updated user1:", user1)
print("Updated user2:", user2)
#Task 4
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 6, 7}

# 1. Union
print("Union:", A | B | C)

# 2. Common
print("Common:", A & B & C)

# 3. Unique
print("Only A:", A - (B | C))
print("Only B:", B - (A | C))
print("Only C:", C - (A | B))

# 4. Update
A.update(B)
A.update(C)
print("Updated A:", A)

