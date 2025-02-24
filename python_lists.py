#list declaration
list = ["apple", "banana", "cherry"]
print(list)

list = ["apple", "banana", "cherry", "apple"]
print(list)
print(len(list))

list1=["apple", "banana", 34, False]
print(list1)

#update at perticular index
list1[0]="cherry"
print(list1)
print(list1[3])
print(list1[-2])
print(list1[1:3])

#checking item in list
if "cherry" in list1:
    print("yes")


list1[1:3]=["orange", 90]
print(list1)

#inserting item at perticular index
list1.insert(3,"lemon")
print(list1)

#inserting item at end
list1.append(40)
print(list1)

#appending two lists or list with any other objects like tuples, dicts sets
list1.extend(list)
print(list1)

#remove a perticular item
list1.remove("apple")
print(list1)

#remove from end
list1.pop()

#remove from index
list1.pop(2)
print(list1)

#deleting item from index
del list1[1]
print(list1)

#making list empty
list.clear()
print(list)

#deleting list
del list

#iterating in list
for x in list1:
    print(x)

#iterating with index
for x in range(len(list1)):
    print(list1[x])

#iterating using list comprehension
[print(x) for x in list1] 

list2= [x for x in list1] 
print(list2)


#sort list
list3=["orange", "mango", "kiwi", "pineapple", "banana"]
list3.sort()
print(list3)

list4=[20,10,50,90]
list4.sort()
print(list4)

#sort in descending order
list4.sort(reverse=True)
print(list4)

#custom sort
def func(n):
    return abs(n-50)

list4.sort(key=func)
print(list4)

#reverse
print(list3)
list3.reverse()
print(list3)


#copy list
list5=list4.copy()
print(list5)

list6= list(list4)
print(list6)

list7=list4[:]
print(list7)
