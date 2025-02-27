#if else elif
a=20
b=30
if a>b:
    print("a is greater")
elif a==b:
    print("both are equal")
else:
    print("b is greater")


#short hand if else
print("a is greater") if a>b else print("b is greater ")

print("a is greater") if a>b else print("both equal") if a==b else print("b is greater")

#and
a=20
b=30
c=40
if a > b and c > a:
  print("Both conditions are True")

#or
if a > b or a > c:
  print("At least one of the conditions is True")

#not
if not a > b:
  print("a is NOT greater than b")


#nested if
a = 30

if a > 10:
  print("Above 10,")
  if a > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 


#pass
if a>b:
   pass