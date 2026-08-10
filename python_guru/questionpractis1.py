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
age = int(input("Enter your age = "))
can_vote= age>=18


senior_citizen=age>=60
print(f" user Can vote= {can_vote}")
print(f" user Senior citizen={senior_citizen}")

# if age >= 60:
#     print("You are a senior citizen")
# elif age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

