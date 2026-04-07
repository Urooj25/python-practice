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
def factorial_loop(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial_loop(5))
def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    #Fibonacci Sequence Har number = pichlay 2 numbers ka sum
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(7))
#Recursion with Lists
def sumlist(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sumlist(numbers[1:])
my_list= [1,2,3,4,5]
print(sumlist(my_list))
#Find the maximum value in a list:
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))
#Recursion Depth Limit
import sys
print(sys.getrecursionlimit())
#If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
       


