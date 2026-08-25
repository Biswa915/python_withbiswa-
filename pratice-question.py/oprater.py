# a=int(input("enter your number="))
# b=int(input("enter your number="))
# print(a+b,a-b,a%b,a*b)


# def biswa(a,b):

#     return f"{a+b},{a-b},{a*b},{a%b}"

# print(biswa(10,20))

# Take a number as input. Print whether it is even or odd using the %
# operator and a comparison operator
# a=int(input("enter your number="))
# c=a%2==0
# print(c)

# Take the users age as input. Check and print whether they are eligible
# to vote (age >= 18) and whether they are a senior citizen (age >= 60).
# Print both results.
user=int(input("enter your age="))
user_vote=user>=18
user_vote2=user>=60
print(f"you age eligible for vote {user_vote} and the senior citizen {user_vote2}")
