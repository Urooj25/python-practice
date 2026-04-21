#Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:
list_comp = [x*x for x in range(5,10)]
print(list_comp)#[25, 36, 49, 64, 81]
#generator expression
gen_exp = (x*x for x in range(5,10))
print(gen_exp)#only memory address dikha gha
print(list(gen_exp))
gen_exp = (x*x for x in range(5,10))
for x in gen_exp:
        print(x)
#Using a generator expression with sum:
total = sum(x*x for x in range(5,10))
print(total)
#Fibonacci Sequence Generator
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34... next number previous two numbers kay sum say bnta ha
#"Without Running Out of Memory" Ka Matlab:
#fib_list = [0,1,1,2,3,5,8,13.....] # infinite list = memory full!
#Fibonacci generator kabhi khatam nahi hota – while True ki wajah se, aur memory bhi nahi bharta kyunki ek ek value deta hai! 
def Fibonacci():
    a,b =0,1
    while True:
        yield a
        a,b = b,a+b
gen = Fibonacci()
for _ in range(100):## _ = "count mujhe nahi chahiye"
    print(next(gen))
    ''' ❌ Yeh dangerous hai
while True:
    print("hello")   # rokne ka koi tarika nahi! crash!'''
#Generator Methods
#The send() method allows you to send a value to the generator:
def echo_generator():
    while True:
        recieved = yield
        print(("recieved",recieved))
gen = echo_generator()
next(gen)#Prime the generator
gen.send("Hello")
gen.send("Urooj")
#close() Method
def my_gen():
    try:#Yahan generator ka asli kaam
        yield 1
        yield 2#Kabhi nahi chale – close ho gaya
        yield 3
    finally:#Band hote waqt ZAROOR chale
        print("generator closed")
gen = my_gen()
print(next(gen))
gen.close()# without finally # koi message nahi – generator chupke band ho gaya 👻#Generator force band karo

