#Python has a built-in package called json, which can be used to work with JSON data.
import json
x = '{"name" : "urooj" , "age" : 21, "city" : "wahcantt"}'
y = json.loads(x)
print(y["age"])
#used in weather apps, APIS transfeer data etc for ex
import json

# Imagine this data came from a weather API
api_response = '{"temperature": 35, "city": "Islamabad", "weather": "sunny"}'

data = json.loads(api_response)  # String → Dictionary
print(data["city"])         # Islamabad
print(data["temperature"])  # 35

# Convert dictionary back to string
text = json.dumps(data)     # Dictionary → String
#Convert from Python to JSON
import  json
x = {
    "name" : "Amna",
    "City" : "Wah",
    "age" : 20
}
y = json.dumps(x)
print(y)
#Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps(["Urooj","Amna"]))
print(json.dumps((1,2,3,4,5)))
print(json.dumps(True))
print(json.dumps(3.14))
print(json.dumps(False))
print(json.dumps(None))#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))#It  prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4, separators=("."," = "), sort_keys=True)
#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)