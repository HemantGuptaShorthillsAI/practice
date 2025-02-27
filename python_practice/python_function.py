def func():
  print("hello")

func()


#arguments
def func1(x):
  print("hi",x)

func1("abc")

def func1(x,y):
  print("hi",x,y)

func1("abc","def")

#arbitrary arguments
def func(*x):
  print("I am " + x[2])

func("abc", "def", "ghi") 

def func3(x1,x2,x3):
  print("helo: "+ x2)

func3(x1="abc", x2="def", x3="ghi")


#**kwargs
def func4(**x):
  print("It is " + x["b"])

func4(a = "abcd", b = "efghi") 

#default parameter
def func1(x="default"):
  print("hi",x)

func1("abc")
func1()

#positional only argument
def my_function(x, /):
  print(x)

my_function(3) 

#keyword only argument
def my_function(*, x):
  print(x)

my_function(x = 3) 

#comnination of both
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8) 


#return
def return_func(x):
  return x

print(return_func(90))


