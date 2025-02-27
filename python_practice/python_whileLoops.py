i = 0
while i < 10:
  print(i)
  i += 1

#break
i = 0
while i < 10:
  if i==5:
    break
  print(i)
  i += 1

#continue
i = 0
while i < 10:
  if i==5:
    i+=1
    continue
  print(i)
  i += 1


#else 
i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("byy")