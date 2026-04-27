#Python has a built-in package called re, which can be used to work with Regular Expressions.
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x)#Sirf shuru se match ^word ,Sirf end pe match word$, Poori string match ^word$,Kahin bhi match word
#Print a list of all matches:
import re   
txt = "The rain in spain"
x = re.findall("ai",txt)
print(x)
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)#empty list
'''The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:'''
import re
txt = "The rain in spain"
x = re.search('\s',txt)#re.search() pehla match dhundta hai,\s matlab koi bhi whitespace (space, tab, newline)
print("The first white-space character is located in position:",x.start())#x.start() match ki starting position return karta hai.
#If no matches are found, the value None is returned:
import re
txt = "The rain in spain"
x = re.search("portugal",txt)
print(x)#None
#The split() function returns a list where the string has been split at each match:
import re
txt = "The rain in spain"
x = re.split("\s",txt)
print(x)#['The', 'rain', 'in', 'spain']
#You can control the number of occurrences by specifying the maxsplit parameter:
import re
txt = "The rain in spain"#
x = re.split("\s",txt,1)
print(x)#['The', 'rain in spain']
#The sub() function replaces the matches with the text of your choice:
import re
txt = "The rain in spain"
x = re.sub("\s","9",txt)
print(x)#The9rain9in9spain
#Replace the first 2 occurrences:
import re
txt = "The rain in spain"
x = re.sub("\s","9",txt,2)##Replace the first two occurrences of a white-space character with the digit 9:
print(x)
#A Match Object is an object containing information about the search and the result.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#Print the position (start- and end-position) of the first match occurrence
import re
txt = "the rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
import re

txt = "The rain in Spain"
x = re.search("Spain",txt)
print(x.span())#12,17 17 issliya aay bcz hm last may +1 krta ha



