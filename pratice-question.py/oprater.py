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
# user=int(input("enter your age="))
# user_vote=user>=18
# user_vote2=user>=60
# print(f"you age eligible for vote {user_vote} and the senior citizen {user_vote2}")

# A student scored marks in 3 subjects. Take all three as input,
# calculate the total and average, and print both using an f-string.

# sub1=int(input("enter a number ="))
# sub2=int(input("enter a number ="))
# sub3=int(input("enter a number ="))
# total=(sub1+sub2+sub3)
# avarage=(total/3)
# print(f"the total number is {total} and avarage {avarage}")

# Q5: Take a number as input. Print the result of that number raised to the
# power of 3 using **. Also print what // 7 and % 7 give for the same number.

# num=int(input("enter a number=" ))
# print(f" power{num**3} and also folt divistion {num//7} and modulas {num%7}")

# Q6: Take two numbers as input. Without using *
# calculate and print their product
# using += in a way that adds the first number to itself the
# second number of times. (Think carefully.)
# use for loop
# num1=int(input("enter your number="))
# num2=int(input("enter your number="))
# total=0
# for i in range(num2):
#     total +=num1
# print(total)

# use while loop
# num1 = int(input("enter your number="))
# num2 = int(input("enter your number="))
# total = 0
# i = 0
# while i < num2:
#     total += num1
#     i+= 1
# print(total)

# Q7: Take a number as input. Print whether it is positive, negative, or zero.
# num=int(input("enter your number="))

# if num>=50:
#   print("positive")
# elif num>=30:
#   print("nagativi")
# else:
#   print("zero")
  
# Q8: Take two numbers as input. Print the greater of the two. If they are
# equal, print "Both are equal
# num1 = int(input("enter your number="))
# num2 = int(input("enter your number="))
# if num1>num2:
#     print(f"{num1} and greater than {num2}")
# elif num2>num1:
#     print(f"{num2} and greater than {num1}")
# else:
#     print("both are equal")


# Q9: Take a student's marks as input. Print their grade based on this scale:
# 90 and above → A
# 75 to 89 → B
# 60 to 74 → C
# 40 to 59 → D
# Below 40 → F

# student=int(input("enter a marks="))
# if student >=90 and student <=100:
#     print("A")
# elif student >=75 and student <=89:
#     print("B")
# elif student >=60 and student<=74:
#     print("C") 
# elif student >=0 and student<=59: 
#     print("D")
# else:
#     print("F")
# 

# Q10: Take a year as input. Check if it is a leap year. A year is a leap
# year if it is divisible by 4, but not by 100, unless it is also
# divisible by 400.      

# year=int(input("enter a year="))
# if  year %400==0:
#     print("it is a leap year ")
# elif year %100==0:
#     print("it is not a leap year")
# elif year %4==0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")

# Q11: Take a persons age and whether they have a valid ID (True/False) as input. They
# can enter a venue only if they are 18 or older AND have a valid ID. Print the
# appropriate message.
# age=int(input("enter your age ="))
# id= input("enter your valid (True/False)=")
# if age >=18 and id == "True":
#      print("you can valid for appropriate")
# else:
#    print("False")

# 

# a=int(input("enter a number ="))
# b=int(input("enter a number ="))
# c=int(input("enter a number ="))
# if a>b and a>c:
#     print("largest number is ",a)
# elif b>a and b>c:
#     print("largest number is ",b)
# else:
#     print("largest number is" ,c)

# Q13: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line.
# num=int(input("enter a number="))
# result = "Even" if num %2 == 0 else "odd"
# print(result)

# Q14: A shop gives discounts based on purchase amount:
# Above 5000 → 20% discount
# Above 2000 → 10% discount
# Above 1000 → 5% discount
# 1000 or below → no discount
# amount=int(input("enter a number="))
# if amount>=5000:
#     discount=amount*(20/100)
# elif amount>=2000:
#     discount=amount*(10/100)
# elif amount>=1000:
#     discount=amount*(5/100)
# else:
#     discount=0
# print("discount=",discount)

# Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100

# a=int(input("enter a number="))
# b=int(input("enter a number="))
# i=a
# while i<=b:
#     if i %3==0 and i %5==0:
#         print(i,end=" ")
#     i+=1

# Q16. Sum of all the numbers from 1 to 100
# a=int(input("enter a number="))
# b=int(input("enter a number="))
# i=a
# total=0
# while i <=b:
#     total =total+1
#     i+=1
# print(f"total={total}")

# Q17. Sum of all the numbers from 1 to 100 divisible by 2 and 7
# a=int(input("enter a number="))
# b=int(input("enter a number="))
# i=a
# total=0
# while i <=b:
#     if i%2==0 and i%7==0:
#      print(i)
#      total =total+1
#     i+=1
# print(f"total={total}")

# Q18. Ask a number from the user, print the multiplication table upto 10
# num=int(input("enter a number="))
# i=0
# while i<=10:
#     div= num*i
#     print(f"{num}x{i}={div}")
#     i+=1
    
# Q19. Ask a number from the user, and print all the factors
# num=int(input("enter a number ="))
# i=1
# while i <=num:
#     if num % i==0:
#         print(i,end=" ")
#     i+=1

# Q20. Take numbers as input from the user one by one. Skip negative
# numbers and keep adding the positive ones. Stop when the user
# enters 0 and print the total. (Uses both continue and break.)

# total=0
# for i in range(50):
#     num=int(input("enter a number ="))
#     if num==0:
#         break
#     if num<0:
#         continue
#     total=num+1
# print(total)
# total=0
# while True:
#     num=int(input('enter your number='))
#     if num == 0:
#         break
#     if num <0 :
#         continue
#     total += num
    
# print(total)

# Q22
'''''
*
* *
* * *
* * * *
* * * * *
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()
'''''
* * * * *
* * * * 
* * * 
* * 
* 
# '''
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# q22
''''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
'''
# for i in range(1,6):
#      for j in range(1,i+1):
#          print(j, end=" ")
#      print()


# q23
''''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
# n=int(input("enter a number="))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()/

# q24
'''''
1 2 3 4 5
1 2 3 4 
1 2 3  
1 2
1
''' 
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# q25
'''''
5 4 3 2 1 
5 4 3 2  
5 4 3
5 4 
5
'''
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()
# q26
'''''
5 4 3 2 1 
4 3 2 1  
3 2 1
2 1
5

'''
# for i in range(5,0,-1):
#      for j in range(i,0,-1):
#           print(j,end=" ")
#      print()
# q27
''''
7 6 5 4 3 2 1 
7 6 5 4 3 2 
7 6 5 4 3
7 6 5 4
7 6 5
7 6
7
'''
# for i in range(1,8):
#     for j in range(7,i-1,-1):
#         print(j,end=" ")
#     print()

# q28
''''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# q29
''''
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 4
5 4 3
5 4
5
'''
# for i in range (5,0,-1):
#     for j in range(5,i-1,-1):
#          print(j,end=" ")
#     print()
# for i in range(1,5):
#      for j in range(5,i,-1):
#          print(j,end=" ")
#      print()

# Q30.
""""
           1
         1 2 3
       1 2 3 4 5
     1 2 3 4 5 6 7
   1 2 3 4 5 6 7 8 9
     1 2 3 4 5 6 7 
       1 2 3 4 5 
         1 2 3
           1

"""
# for i in range(1,6):
#     for j in range(1,5-i +1):
#         print(" ",end=" ")
#     for k in range(1,(i*2) -1+1):
#          print(k,end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,5-i +1):
#         print(" ",end=" ")
#     for k in range(1,(i*2)-1+1):
#          print(k,end=" ")
#     print()

# Q31
''''
1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15 
'''
# num=int(input("enter a number ="))
# total=1
# for i in range(1,num+1):
#     for j in range(i):
#        print(total,end=" ")
#        total+=1
#     print()

# q32
''''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
# for i in range(1,6):
#     for j in range(1,6):
#          print(j,end=" ")
           
#     print()

# Q33
''''
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
'''
# for i in range(1,6):
#     for j in range(1,6):
#         if(i+j)%2==0:
#           print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
# q34
''''
* * * * *
*       *
*       *
*       *
* * * * *
'''
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()