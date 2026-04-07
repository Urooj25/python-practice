#Recursion matlab — apna kaam chhhota karke, wahi kaam dobara khud karo — jab tak kaam khatam na ho jaye!
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)
countdown(3)
#Every recursive function must have two parts:A base case - A condition that stops the recursionA recursive case - The function calling itself with a modified argumentWithout a base case, the function would call itself forever, causing a stack overflow error.
def fictoral(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fictoral(n-1)
print(fictoral(5))
#Loop aur Recursion dono baar baar kaam karte hain — lekin Recursion mein function khud ko call karta hai, koi for ya while nahi hota!
