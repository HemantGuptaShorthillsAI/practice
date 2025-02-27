#variables not need datatype declaration
x = 5
y = "Hey"
print(x)
print(y)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
print(x)
print(y)
print(z)

#case sensitive
a=9
A='hi'
print(A)
print(a)

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x,y,z)
print(x+y+z)

#global variables
x = "abc"

def func():
  x = "def"
  print("Hlo " + x)

func()

print("Hlo " + x)

def func():
  global x
  x = "ghi"

func()

print("HLO " + x) 