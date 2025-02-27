# tuple1=("abc","def","ghi")
# x=iter(tuple1)
# print(next(x))
# print(next(x))

# a="hemant"
# x=iter(a)
# print(next(x))
# print(next(x))
# print(next(x))


#iterartor creation
class MyNumbers:
  def __iter__(x):
    x.a = 1
    return x

  def __next__(x):
    y = x.a
    x.a += 1
    return y

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 


#iterator stoping
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)