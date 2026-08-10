# Practice Questions

# Q1: Take two numbers as input from the user. Print their sum, difference,
# product, and remainder.

# num1 = int(input("enter first number 1="))
# num2 = int(input("enter second number 2="))
# print(f"sum = {num1 + num2}")
# print(f"difference = {num1 - num2}")
# print(f"product = {num1 * num2}")
# print(f"remainder = {num1 % num2}")

# Q2: Take a number as input. Print whether it is even or odd using the %
# operator and a comparison operator.
# num = int(input("enter a number:"))
# print(num % 4 == 0)

# Q3: Take the user's age as input. Check and print whether they are eligible
# to vote (age >= 18) and whether they are a senior citizen (age >= 60).
# Print both results.
# age = int(input("Enter your age = "))
# can_vote= age>=18


# senior_citizen=age>=60
# print(f" user Can vote= {can_vote}")
# print(f" user Senior citizen={senior_citizen}")

# if age >= 60:
#     print("You are a senior citizen")
# elif age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Q4: A student scored marks in 3 subjects. Take all three as input,
# calculate the total and average, and print both using an f-string.
# sub1=int(input("Enter marks for subject 1: "))
# sub2=int(input("Enter marks for subject 2: "))
# sub3=int(input("Enter marks for subject 3: "))
# total=sub1 + sub2 + sub3
# average=total/3
# print(f"Total mark = {total}")
# print(f"Average mark = {average}")
# Q7: Take a number as input. Print whether it is positive, negative, or zero.
# num = int(input("Enter your number: "))
# if num >0:
#     print("positive")
# elif num <0:
#     print("negative")
# else:
#     print("both are zero")

# Q8: Take two numbers as input. Print the greater of the two. If they are
# equal, print "Both are equal."
# num1= int(input("Enter your number="))
# num2= int(input("Enter your number="))

# if num1 > num2:
#     print(f"{num1} is geater than{num2}")
# elif num2>num1:
#     print(f"{num2} is gater than{num1}")
# else:
#     print("Both are equal") 

# Q9: Take a student's marks as input. Print their grade based on this scale:
# · 90 and above -> A
# · 75 to 89 -> B
# . 60 to 74 -> C
# · 40 to 59 -> D
# . Below 40 -> F
mark =int(input("Enter your mark"))
if mark >=90:
    print("A")
elif mark >=75 and mark <=89:
    print("B")
elif mark >=60 and mark <=74:
    print("C")
elif mark >=40 and mark <=59:
    print("D")
elif mark >=40:
    print("f")  
else:
    print("not valied number")   
           