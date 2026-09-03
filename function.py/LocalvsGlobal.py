# Local vs Global
# Scope refers to where a variable is accessible in your code. A variable created
# inside a function is local it only exists inside that function. A variable created
# outside all functions is global it can be accessed from anywhere.


#Local Variable 1
def num(a,b,c):
     total=a+b+c
     print(f"total mark={total}")


num(10,15,20)

#Local Variable 2
def num(n1,n2):
     n1=100
     n2=120
     print(f"n1={n1} and n2={n2}")
n1=10
n2=20
num(n1, n2)
print(n1)
print(n2)

#Global Variable 1
n=10
n1=20
def num():
     total=n+n1
     print(f"total={total}")

num()

name="biswa"
def biswa():
     print(f"hey {name} good morning")

biswa()