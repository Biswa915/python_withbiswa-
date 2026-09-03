# Local vs Global
# Scope refers to where a variable is accessible in your code. A variable created
# inside a function is local it only exists inside that function. A variable created
# outside all functions is global it can be accessed from anywhere.


#Local Variable
def num(a,b,c):
     total=a+b+c
     print(f"total mark={total}")

     
num(10,15,20)