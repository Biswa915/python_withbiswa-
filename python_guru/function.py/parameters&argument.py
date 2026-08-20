# Parameters and Arguments
# A parameter is a variable listed inside the function definition. An argument
# is the actual value you pass when calling the function. Parameters make
# functions flexible - the same function can work with different data every time.
# example: 
# def greet(name):
#     print(f"hello {name}!")
# greet("biswa")    


# parameter 3 int as a ,print thhe total
# def addition(a,b,c):
#    print(f"name is {a} and age {b} gender is {c}")
# n=input("enter your name=")
# a=int(input("enter your name="))
# g=input("enter your gender=")
# addition(n,a,g)   

def greet(n1,n2):
   print(f"total={n1+n2}")
greet(20,40)