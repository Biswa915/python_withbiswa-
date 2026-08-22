# return Statement
# The return statement sends a value back to whoever called the function.
# Without return, a function just does something but gives nothing back.
# With return, you can use the result in the rest of your program.

# example-
# def num(n1,n2,n3):
#     return n1+n2+n3

# ans=num(10,50,32)
# print(ans)

# true and false return statement
# def can_voter(age):
#     if age>18:
#         return True
#     return False

# ans=can_voter(19)
# print(ans)

# print(can_voter(10))

def greed(name,age,gender):
    return f"my name is {name} and i am {age} year old and gender {gender}"


ans=greed("Biswajit",23,"male")
print(ans)
