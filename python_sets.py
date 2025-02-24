#declaration of set
set1={"apple", "banana", "cherry"}
print(set1)
#unordered
#unchangeable
#no duplicates

set2={"apple", "banana", "cherry","apple",False,0}
print(set2)

set3=set(("abc","def"))
print(set3)

#access items
for x in set1:
  print(x) 

set1.add("kiwi")
print(set1)

#add sets
set2 = {"pineapple", "mango", "papaya"}
set1.update(set2)
print(set1)

list1=["orange","grapes"]
set1.update(list1)
print(set1)

#remove item
set1.remove("kiwi")
print(set1)
set1.pop()
print(set1)

#loop item
for x in set1:
  print(x)


#joins in set
set={"abc","def","orange"}
set3=set1.union(set2)
print(set3)

set3=set1 | set2
print(set3)

set4=set1.union(set2,set3)
print(set4)

set3= set1&set2
print(set3)

set3= set1.intersection(set2)
print(set3)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#difference
set3 = set1-set2
print(set3)