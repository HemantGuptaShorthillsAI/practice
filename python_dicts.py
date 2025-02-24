#declaring dictionaries
dict1 = { "brand": "Ford","model": "Mustang","year": 1964 }
print(dict1)

print(dict1["brand"])

#no duplicates

dict1 = { "brand": "Ford","model": "Mustang","year": 1964 , "colors": ["red", "white", "blue"]}
print(type(dict1))
print(dict1)

#access items
x=dict1.get("colors")
print(x)

x=dict1.keys()
print(x)

x=dict1.values()
print(x)

print(dict1.items())

#update dict
dict1.update({"year":2024})
print(dict1)

#remove items
dict1.popitem()
print(dict1)

#copy dict
dict2=dict1.copy()
print(dict2)

#looping
for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)

for x in dict1:
    print(x)

for x, y in dict1.items():
  print(x, y) 


#nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

print(myfamily["child2"]["name"]) 