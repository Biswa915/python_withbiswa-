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

# def greet(n1,n2):
#    print(f"total={n1+n2}")
# greet(20,40)

            #                 1>       :Default Arguments:
            #  A default argument is a value that a parameter takes automatically if no
            #    argument is passed for it when calling tle function. It makes certain
            #                        parameters optional.

                    # 2>  and Keyword Arguments

# Default Arguments
# def calculet_mark(eng,psy,math=0):
#     print(f"eng={eng}")
#     print(f"psy={psy}")
#     print(f"math={math}")
#     total=(eng+psy+math)
#     print(f"total={total}")

# calculet_mark(10,20)

def calculet_mark(eng,psy=0,math=0):
    print(f"eng={eng}")
    print(f"psy={psy}")
    print(f"math={math}")
    total=eng+psy+math
    print(f"total={total}")

calculet_mark(psy=10,eng=20,)

