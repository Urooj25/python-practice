#Generators are functions that can pause and resume their execution.
#he code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
def my_generater():
    yield 1 # pehli baar: 1 do, ruk jao
    yield 2 # doosri baar: 2 do, ruk jao
    yield 3 # teesri baar: 3 do, khatam
for value in my_generater():
    print(value)
#return saari cheez ek baar deta hai, yield thodi thodi karke deta hai – jab zaroorat ho tabhi! 
# Normal function – saari values EKAATH deta hai
def normal():
    return [1, 2, 3]  # poori list memory mein

# Generator – EK EK karke deta hai
def generator():
    yield 1   # sirf 1 memory mein
    yield 2   # sirf 2 memory mein
    yield 3   # sirf 3 memory mein
    #Normal function = poori kitaab photocopy karo, phir parho 📚
#Generator = ek ek page parho, agli page tabhi lo jab chahiye 📖
#The yield Keyword
def count_upto(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_upto(6):
    print(num)
#Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:
def large_sequence(n):
    for i in range(n):
        yield i
gen = large_sequence(100000)
print(next(gen)) #0
print(next(gen))#1
print(next(gen))#output 0 1 2 bcz ek ek krkay store krta ha next bol rha ha agla du