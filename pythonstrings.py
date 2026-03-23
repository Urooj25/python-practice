#Strings concatentation
a = "Urooj"
b = "Fatima"
c = a +" "+b
print(c)
#To add a space between them, add a " "
#Python - Format - Strings
x = 35
y = f"My age is:{x}"

print(y)
#Place holders 
price = 59
txt = f"The price is {price} dollers"
print(txt)
#Modifier
Cost = 67
Price = f"The price is {Cost:.3f} dollers"
print(Price)
#A placeholder can contain Python code, like math operations:
Rate = f"The rate is {45+50} and {45*56} and{34-87} and{34/45} "
print(Rate)
#Python Escape Characters
#To insert characters that are illegal in a string, use an escape character.
Name = "My name\t is \"Urooj\" Fatima"
print(Name)
#Single quote
print("It\'s a beautiful day!")
#Backspace (\b) deleteprevoious alphabet
print("My name is Urooj\b Fatim\'a")
#Carriage Return (\r)
#Ye cursor ko wapas line ke shuru mein le aata hai aur agla text purane text ke upar overwrite kar deta hai.
print("python is fun\rCoding")
#Hex (\xhh) aur Octal (\ooo) values
#Ye specific symbols ya characters print karne ke liye unka code use karte hain.
print("\x50\x49")
##A backslash followed by three integers will result in a octal value:
print('\767\667')
#Code Challenge
print("Name:\t Urooj\nField:\t \"Enginerring\"\nPath:\t D:\\Projects\\Python\n")
#String method
Title = "Our  search project is Al model for diabetes pridiction"
print(Title.upper())
print(Title.lower())
print(Title.title())
print(Title.capitalize())
print(Title.swapcase())
#Search & Find Methods
print(Title.find("search"))#-1 if not present
print(Title.index("search"))#Error on not present
print(Title.startswith("MY"))
print(Title.endswith("MODEL"))
print(Title.count("search"))
#Code Challenge
txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())
name = "Python"
print(f"I love {name}")
