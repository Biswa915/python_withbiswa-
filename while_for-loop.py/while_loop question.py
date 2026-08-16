# Practice Questions on WHILE Loop
# Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100.

# Q16. Sum of all the numbers from 1 to 100.

# Q17. Sum of all the numbers from 1 to 100 divisible by 2 and 7.

# Q18. Ask a number from the user, print the multiplication table upto 10

# Q19. Ask a number from the user, and print all the factors.

#Q15
# start=int(input("enter your number="))
# end=int(input("enter your number="))

# i=start
# while i <=end:
#     if i %3 ==0 and i %5==0:
#          print(i, end=" ")
#     i +=1

#q16
# start=int(input("enter your number="))
# end=int(input("enter your number="))

# i=start
# total = 0
# while i<=end:
#      total= total+i
#      i+=1

# print(f"total = {total}")

#q17
# start=int(input("enter your number="))
# end=int(input("enter your number="))

# i=start
# count = 0 # total=0
# while i<=end:
#      if i % 2==0 and i%7==0:
#        print(i)
#        count= count+1 #/ total= total+i
#      i+=1
     
# print(f"total count 2 and 7 = {count}") # print(f"total{total}"")

# Q18  :
# num=int(input("enter your number="))
# i=1
# while i<=10:
#     div= num*i
#     print(f"{num}x{i}={div}")
#     i +=1

# Q19 
num=int(input('enter your num='))
i=1
count=0
while i<=num:
    if num %i==0:
     count=count+i
    i+=1
print(f'total factor number{num} and counting number{count}')



     