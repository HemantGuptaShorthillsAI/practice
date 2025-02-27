for x in "banana":
  print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range()
for x in range(5):
  print(x)

#else
for x in range(5):
  print(x)
else:
  print("by")

#nested loop

x = ["abc", "def", "ghi"]
y = ["jkl", "mno", "pqr"]

for a in x:
  for b in y:
    print(a, b) 