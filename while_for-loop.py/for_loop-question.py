# Practice Questions on for Loop
# # Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100.

# # Q16. Sum of all the numbers from 1 to 100.

# # Q17. Sum of all the numbers from 1 to 100 divisible by 2 and 7.

# # Q18. Ask a number from the user, print the multiplication table upto 10

# # Q19. Ask a number from the user, and print all the factors.

# Q1
# start = int(input("Enter start number = ")) 
# end=int(input("Enter end number = ")) 

# count=0
# for i in range (start,end):
#     if i %3 ==0 and i %5==0:
#         print(i,end=" ")
#         count +=1
# print(f" count of number division {count}")

# q2
# start=int(input("enter your number="))
# end=int(input("enter your number="))

# total=0
# for i in range(start,end+1):
#     total +=i
# print(f"sum ={total}")

# q3
# start=1
# end=100
# for i in range(start,end+1):
#     if i %2==0 and i %7==0:
#         print(i,end=" ")

# Q4
num=int(input("enter your number="))
for i in range(1,18):
    ans= num*i
    print(f"{num}x{i}={ans}")