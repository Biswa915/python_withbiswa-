# Practice Questions on Parameters and Arguments

# Q37. Write a function called add that takes two numbers as parameters
# and prints their sum.

# Q38. Write a function called rectangle_area that takes length and breadth
# as parameters and prints the area.

# Q39. Write a function called find max that takes three numbers as
# parameters and prints the largest one.

# Q40. Write a function called discount_price that takes original_price
# and discount_percent as parameters and prints the final
# price after discount ..


# q1
# def addition(a1,b1):
#     ans=a1+b1
#     print(f'total={ans}')

# addition(123,43)

# q2
# def rectangle_area(length,breadth):
#     area=length*breadth
#     print(f"area of rectangle{area}")

# rectangle_area(10,12)
# rectangle_area(2 ,3)

# q3
# def max(a,b,c):
#     if a>=20:
#         print(a)
#     elif b>=30:
#         print(b)
#     else:
#         print(c)

# max(10,50,34)

# q4
# def discount_price(original_pice,discount_price):
#     discount=(discount_price /100 ) * original_pice
#     final_amount= original_pice - discount
#     print(f"the final price Rs{discount}")
#     print(f"the final price Rs{final_amount}")

# discount_price(475, 58)


# Practice Questions on Return Statements

# Q41. Write a function called square that takes a number and returns its square.
# Store the result and print it.

# Q42. Write a function called min_of_three that takes three numbers and returns
# the smallest without using any built-in function.

# Q43. Write a function called absolute_value that takes a number and returns
# its absolute value without using the built-in abs() function.

# q41
# def squer(a):
#     return a**2

# print(squer(19))

# Q42
# def min_of_three(n1,n2,n3):
#     if n1<n2 and n1<n3:
#         return n1
#     elif n2<n1 and n2<n3:
#         return n2
#     return n3

# print(min_of_three(8,10,15))

# q43
# def absolute_value(num):
#     return abs(num)

# print(absolute_value(-100))
# print(absolute_value(100))
# print(absolute_value(-100))

#  Practice Questions on LAMBDA Functions

# Q44. Write a lambda function that takes a number and returns its cube. Store
# it in a variable and call it.

# Q45. Write a lambda function that takes a number and returns "Positive", or
# "Negative".

# q44
# a=int(input("enter a number="))
# cube=lambda a:a**3
# print(cube(a))

# q45
# num=int(input("enter a number="))
# bisw=lambda num: "Positive" if num>0 else "Negative"
# print(bisw(num))

# Practice Questions Functions (Assignments)
# Q46. Write a function fizzbuzz(n) that takes a single number and prints "Fizz
# if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible
# by both, otherwise print the number itself.

# a = int(input("enter a number="))
# def fizzbuzz(n):
#     if n % 3 ==0 and n % 5 ==0:
#         print("FIZZbuzz")
#     elif n % 3 ==0:
#         print("FIZZ")
#     elif n % 5==0:
#         print("buzz")
#     else:
#         print(n)

# fizzbuzz(a)

# Practice Questions Functions (Assignments)

# Q47. Write a function power(base, exp) that returns base raised to exp using a
# loop - no ** operator or pow() allowed.

# Q48. Write a function tax_calculator(income) that takes annual income and returns
# the tax amount based on these slabs:
# · Up to 2,50,000 -> No tax
# · 2,50,001 to 5,00,000 -> 5%
# · 5,00,001 to 10,00,000 -> 20%
# · Above 10,00,000 -> 30%


# Q47.
def power(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result


print(power(4,7))
