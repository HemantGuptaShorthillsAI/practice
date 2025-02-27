#tuples declaration
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

tuple1 = tuple(("apple", "banana", "cherry")) 
print(tuple1)

print(tuple1[2])

#change tuple value
""" ERROR
tuple1[1]="helo"
print(tuple1)
tuples are immutable
"""
x=list(tuple1)
x[1]="helo"
tuple1=tuple(x)
print(tuple1)

#add items
x=list(tuple1)
x.append("banana")
tuple1=tuple(x)
print(tuple1)

tuple2=("kiwi",)

tuple1+=tuple2
print(tuple1)

#remove item
x=list(tuple1)
x.remove("helo")
tuple1=tuple(x)
print(tuple1)

#delete the entire tuple 
#del tuple1

#unpacking a tuple
(a,b,*c,d)=tuple1
print(a)
print(c)

(e,*f)=tuple1
print(e)
print(f)


#looping through tuple
for x in tuple1:
    print(x)

i=0
while i<len(tuple1):
    print(tuple1[i])
    i+=1

#join tuples
tuple2=("hi", "helo")
tuple3=tuple1+tuple2
print(tuple3)

#multiply tuples
tuple3= tuple2*2
print(tuple3)