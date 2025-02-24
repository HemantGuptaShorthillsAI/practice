a = "Hello"
print(a) 

#multiline string
a='''asdfghjkl
qwertyuiop
zxcvbnm
'''
print(a)

#string as array
print(a[7])

#looping through string
a="hello"
for x in a:
    print(x)

#length of string
print(len(a))

#check in string
print("lo" in a)

#if statements
if 'lo' in a:
    print("yes")

if 'ol' not in a:
    print("yes")


#string slicing
a="hello world"
print(a[5:8])
print(a[:4])  #from start
print(a[5:])  #till end


#negative indexing
print(a[-8:-2])

#upper case
print(a.upper())

#lower case
print(a.lower())

#remove space at end and begin
a=" hello word "
print(a.strip())

#replace string
print(a.replace("h","y"))

#split string
print(a.split("o"))

#concatination
a="hello"
b="world"
c=a+b
print(c)
c=a+" "+b
print(c)




age = 36
txt = "My name is John, I am " + str(age)
print(txt)

txt = f"My name is John, I am {age:}" 
print(txt)

txt = f"My name is John, I am {age:.2f}" 
print(txt)

#escape characters
c="hello i am a \"developer\" in shorthills"
print(c)

c="hello i am a \\developer in shorthills"
print(c)

c="hello i am a \ndeveloper in shorthills"
print(c)

c="hello i am a \r dev"
print(c)