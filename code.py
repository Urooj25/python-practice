import mymodule
mymodule.greeting("urooj")
import mymodule
a = mymodule.person1["name"]
print(a)
import mymodule as md
b = md.person1["class"]
print(b)
#Built-in Modules
import platform
x = platform.system()
y = platform.version()
z = platform.machine()
a = platform.processor()
b = platform.python_version()
print(x)#windows
print(y)
print(z)
print(a)
print(b)#platform module aapko system ki info deta hai taake aap smart, adaptive code likh sako jo har OS pe sahi kaam kare! 
#Using the dir() Function
import platform
x = dir(platform)
print(x)#Jab documentation nahi pata — 
() #chalao, dekho kya available hai, phir use karo! Yeh developer ka cheat code hai! #The dir() function can be used on all modules, also the ones you create yourself.
import os
x = dir(os)
print(x)
import math
print(dir(math))
#You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1
print(person1["class"])
